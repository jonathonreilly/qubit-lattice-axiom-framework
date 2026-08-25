---
claim_id: two_axis_opposite_yprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py
---

# Cyclic Next/Prev Lex-Smallest Outgoing Determinant Orientation Of The 1-In 2-Out Frame At t+1 Reverse And Face On Four Y-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** cyclic next/prev lex-smallest outgoing determinant orientation of
the 1-in 2-out frame of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ=t+1`, and reverse/face from that sign, on the
four y-probes of the two-axis opposite seed in `B_3(0)={n:n·n<=9}`. Same
process and y-probes as nm2ax. `M`, `O`, split as nm2ax12. Cyclic as
nm2oricyccz (lex-smallest on next and prev). Let `t(q)` be the formation
tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest
incoming nearest-neighbor steps at `q` using only records with tick
`<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing dual
of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed
and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). Split HOLD required. When split
HOLDs, `m` is the unique vector in `M`. Let `i` in `{1,2,3}` be the axis
index of `m`. `e_next = e_{i+1}` with `3+1→1`. `e_prev = e_{i-1}` with
`1−1→3`. `O_next = O ∩ {±e_next}`. `O_prev = O ∩ {±e_prev}`. If either
is empty, Orient fails, not `UNDEFINED`. Order `+e < −e`. `o_next` is the
lex-smallest vector in `O_next` (hence `+e` if both signs). `o_prev`
likewise. `Orient(q)` is the sign of the integer determinant of the 3×3
matrix with columns `m`, `o_next`, `o_prev`. If split fails, Orient fails,
not `UNDEFINED`. Reverse HOLDs if and only if `Orient(A)=Orient(B)` both
`±1`. Face HOLDs if and only if `Orient(C)=Orient(D)` both `±1`. Cover
and split do not score handedness. This is not leftover of nm2ax
axis-cover. This is not leftover of nm2ax12 1-in 2-out split. This is not
leftover of lexicographic `o1,o2`. This is not leftover of nm2orioney
lex-one. This is not leftover of nm2oricyclz cyclic lex-largest. This is
not leftover of nm2orichy opposite-pair leftover-axis. This is not leftover
of nm2oridetz unique signed outgoing letters with `|O_i|=1`. This is not
leftover of leftover-of-`M` alone. This is not leftover of leftover-of-`O`
alone. This is not leftover-empty fail of leftover axis. This is not leftover
of nmunopp union. This is not leftover of nmt2opp `M` frozen at `t`. This
is not leftover of nmot2opp two-tick composition. This is not leftover of
nmoutopp untimed eventual-`O`. This is not leftover of mixed #7188
fail/fail. This is not leftover of the 1-axis opposite two-site seed. This
is not leftover of the same-lock two-site seed. This is not the two-tick
lock-count clock composition. The second pair is a new seed, not a formed
child. Uniqueness is not required. Mixed remains a set. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py)

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
Split is cover together with `|Axis(M)|=1`. The cyclic oriented frame is
the integer sign of `det(m,o_next,o_prev)` with unique signed incoming
letter `m` and the lex-smallest signed outgoing letter on each cyclic slot
of `Axis(m)` under `+e < −e`. Reverse and face are scored on equal `±1`
signs at the paired probes. Named signs `{+,−}` of locks are a coarser
readout and are not used as the object. A singleton unique outgoing lock
letter is a different readout and is not used as the object. Unsigned axis
units of `Axis(O)` are a different readout and are not used. Unique signed
outgoing letters with `|O_i|=1` are a different readout and are not used.
Lex-one signed letters in axis order `e1<e2<e3` are a different readout
and are not used. Cyclic lex-largest letters on the same slots are a
different readout and are not used. Opposite-pair leftover-axis orientation
is a different readout and is not used. Existential opposite of signed
locks is a different readout and is not used. Axis-cover without the frame
sign is a different readout and is not used. 1-in 2-out split without the
frame sign is a different readout and is not used. Leftover-empty fail of
unsigned leftover axis sets is a different readout and is not used. A
`Z^3` sum of those locks is a different readout and is not used. Occupancy
of sites is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four y-probes of the two-axis opposite seed, Orient +1,+1,+1,fail, reverse hold and face fail from equal +/-1 signs; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_yprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face
target_blocker_text: "display cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame reverse/face on the four y-probes of the two-axis opposite seed, not lex-one axis order, not cyclic lex-largest, not unique |O_i|=1, not leftover axis, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 displayed; do not write Orient into Admissibility, do not reduce to lexicographic o1,o2, do not reduce to nm2orioney lex-one, do not reduce to nm2oricyclz cyclic lex-largest, do not reduce to opposite-pair leftover-axis, do not reduce to unique signed |O_i|=1, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by unique outgoing letters, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four y-probes of the two-axis opposite seed and reverse/face from that sign; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose cyclic
next/prev lex-smallest outgoing determinant orientation of `M` and `O` is
scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nm2ax.

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

## Named cyclic next/prev lex-smallest determinant of `M` and `O` at `τ=t+1`

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

Oriented frame at the same cut:

```text
When split HOLDs, m is the unique signed letter in M.
i in {1,2,3} is the axis index of m.
e_next = e_{i+1} with 3+1→1. e_prev = e_{i-1} with 1−1→3.
O_next = O ∩ {±e_next}. O_prev = O ∩ {±e_prev}.
If O_next or O_prev is empty, Orient fails, not UNDEFINED.
o_next is lex-smallest in O_next under +e < −e (hence +e if both signs).
o_prev likewise.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

The outgoing pair is signed and cyclically ordered from `Axis(m)`, not
ordered by `e1<e2<e3`. Mixed opposite signs on one cyclic slot do not make
Orient fail: lex-smallest picks `+e` over `−e`. Unique outgoing letters of
the whole set `O` are not required: mixed `O` remains a set, and
unique-letter readout of mixed `O` is `UNDEFINED` while this Orient can be
`±1`. Unique signed letters per axis with `|O_i|=1` fail when an opposite
pair occupies that axis; lex-smallest does not. Lex-one in axis order
swaps the cyclic columns when `i=2`, so `det(m,o_j,o_k)` at `C` is `−1`
while this `det(m,o_next,o_prev)` is `+1`. Cyclic lex-largest on the same
slots picks `−e` over `+e` when both signs sit in a slot. A vanishing
determinant is fail. Sign of a nonzero integer determinant is `+1` or
`−1`. Split HOLD required: 2-in 1-out is Orient fail, not UNDEFINED.

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` and both
signs are `±1`. Face oriented frame holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse here as a three-axis occupation
bit, while this reverse HOLDs because both signs are `+1`; lexicographic
reverse fails with `−1,+1` on the same cover HOLD. Identifying split reverse
with this reverse is refused on the same grounds. Identifying leftover-empty
fail with this reverse is refused: leftover-empty reverse fails while this
reverse HOLDs. Identifying unique signed `|O_i|=1` with this reverse is
refused: unique signed reverse fails because `|O ∩ {±e_3}|=2` at `B`, while
cyclic lex-smallest reverse HOLDs. Identifying lexicographic unsigned
`o1,o2` with this reverse is refused: lexicographic reverse fails and this
reverse HOLDs. Identifying nm2orioney lex-one with this reverse is refused:
lex-one reverse HOLDs on the same pair `A,B` but lex-one Orient at `C` is
`−1` while this Orient at `C` is `+1`. Identifying nm2oricyclz cyclic
lex-largest with this reverse is refused: cyclic lex-largest reverse fails
with `+1,−1` on the same cyclic slots. Identifying opposite-pair
leftover-axis orientation with this reverse is refused: leftover-axis reverse
fails from no opposite pair at `A`, while this reverse HOLDs. Identifying a
named sign of those locks with reverse or face is refused: named-sign
lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, `i`, `o_next`, `o_prev`, and Orient at `τ=t+1`

On this process the four y-probes form. Compare to leftover axis: leftover
of the union is empty at `A`, `B`, and `C`, leftover `{e_2}` at `D`,
leftover reverse fail and leftover face fail. Compare to nm2ax axis-cover
and nm2ax12 1-in 2-out split: both HOLD reverse and fail face on this
member. Compare to lexicographic `o1,o2`: that readout scores
`Orient(A)=−1` and `Orient(B)=+1` from the unsigned outgoing 2-plane.
Compare to nm2orichy opposite-pair leftover-axis: that readout scores
Orient fail at `A` from no opposite pair. Compare to nm2oridetz unique
signed `|O_i|=1`: unique signed Orient at `A` is `+1` and at `B` is fail.
Compare to nm2orioney lex-one: that readout scores `Orient(C)=−1` from axis
order `e1<e2<e3`. Compare to nm2oricyclz cyclic lex-largest: that readout
scores `Orient(B)=−1` from `−e_3` on the prev slot. This display reads the
cyclic next/prev lex-smallest outgoing determinant of those same timed
sets:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_3}
O(A, τ) = {+e_2, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
split(A) = hold
split(B) = hold
split(C) = hold
split(D) = fail
m(A) = −e_1
i(A) = 1
o_next(A) = +e_2
o_prev(A) = −e_3
det(A) = 1
Orient(A) = +1
m(B) = +e_1
i(B) = 1
o_next(B) = +e_2
o_prev(B) = +e_3
det(B) = 1
Orient(B) = +1
m(C) = +e_2
i(C) = 2
o_next(C) = +e_3
o_prev(C) = +e_1
det(C) = 1
Orient(C) = +1
m(D) = −e_3
i(D) = fail
o_next(D) = fail
o_prev(D) = fail
det(D) = fail
Orient(D) = fail
```

`A` is a seed at tick 0 with seed letter `−e_1`. Mixed remains a set:
`O(A,τ)` has two outgoing steps and `O(B,τ)` has three outgoing steps.
Unique outgoing letters would assign `UNDEFINED` at mixed `O`. Here
uniqueness is not required. At `A`, split HOLDs, `i=1`, `e_next=e_2`,
`e_prev=e_3`, each cyclic slot has a unique signed letter, and
`det(−e_1,+e_2,−e_3)=1`. At `B`, split HOLDs, `i=1`, `O` has both
`±e_3`, so unique signed fails, not `UNDEFINED`, while lex-smallest picks
`+e_3` over `−e_3` and `det(+e_1,+e_2,+e_3)=1`. At `C`, split HOLDs,
`i=2`, `e_next=e_3`, `e_prev=e_1`, two opposite pairs sit in `O`,
lex-smallest picks `+e_3` and `+e_1`, and `det(+e_2,+e_3,+e_1)=1`. Lex-one
axis order at `C` would read `det(+e_2,+e_1,+e_3)=−1`. At `D`, pair HOLDs
on `{+e_1,−e_1}` but split fails from cover fail with leftover `{e_2}`
(1-in 1-out). Split HOLD is required, so Orient at `D` is fail, not
`UNDEFINED`, and `i(D)`, `o_next(D)`, `o_prev(D)`, and `det(D)` are fail.
Cover and split HOLD reverse on this member and do not score that
`Orient(A)=+1` while lexicographic Orient at `A` is `−1`. O is not M.

On the 1-axis opposite two-site seed, `B` forms at tick 2 and `D` at tick
3, and `D` is 2-in 1-out, so split fails at `D` and Orient at `D` is fail,
not UNDEFINED. That is leftover of the first pair. Here both `(0,0,1)` and
`(0,1,1)` are seeds of a second opposite pair on a second axis, and
`t(D)=2`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,1)` is a
seed, so it is not a new 6-NN of `A`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at `A`, `B`, and
`C`. At `D`, `O` at `t` is `{−e_1}` and grows to `{+e_1, −e_1}` at `t+1`.
Orient at `t` is fail, not UNDEFINED.

## Theorem 2 — reverse from oriented frame at `τ`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. `Orient(A)=+1` and `Orient(B)=+1`. Reverse holds. This is HOLD
iff equal `±1` signs, not leftover of nm2ax axis-cover, not leftover of
nm2ax12 1-in 2-out split, not leftover of lexicographic `o1,o2`, not leftover
of nm2orioney lex-one, not leftover of nm2oricyclz cyclic lex-largest, not
leftover of nm2orichy opposite-pair leftover-axis, not leftover of
nm2oridetz unique signed, not leftover-empty fail, and not exist-opposite.

Reverse oriented frame at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Lexicographic reverse fails because lexicographic `Orient(A)=−1` and
`Orient(B)=+1`. Opposite-pair leftover-axis reverse fails because
`Orient(A)` is fail from no opposite pair in `O`. Unique signed reverse
fails because unique signed Orient at `B` is fail from `|O ∩ {±e_3}|=2`.
Cyclic lex-largest reverse fails because cyclic lex-largest Orient at `B`
is `−1` from `o_prev=−e_3`. Signed cyclic lex-smallest reverse HOLDs
because both signs are `+1`. Lex-one reverse also HOLDs on `A,B`, but
lex-one is not this letter: it scores `Orient(C)=−1` from axis order.
Leftover-empty reverse fails because leftover of the union is empty at `A`
and at `B`. Leftover of `M` reverse HOLDs because leftover of `M` at `A`
and at `B` is `{e_2, e_3}`: nonempty and equal. Leftover of `O` reverse
HOLDs because leftover of `O` at `A` and at `B` is `{e_1}`: nonempty and
equal. Exist-opposite reverse of signed `M` holds. Exist-opposite reverse of
signed `O` holds. Presence of an opposite pair in `O` fails at `A` and
HOLDs at `B`, so pair-presence reverse fails while this reverse HOLDs.
Those leftovers are not this display.

Reverse holds.

## Theorem 3 — face from oriented frame at `τ`

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
`Orient(C)=+1` and `Orient(D)` is fail. Face fails.

Face oriented frame at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Cyclic lex-smallest oriented face fails because Orient
fails at `D` from split fail. Pair face HOLDs while Orient face fails:
split HOLD is required. On the 1-axis opposite two-site seed, cover face
HOLDs while split face fails, and Orient at `D` is fail, not UNDEFINED.
This two-axis member is not leftover of that 1-axis split face fail: here
`t(D)=2` and `M(D)` is singleton `{−e_3}`, whereas the 1-axis child has
`t(D)=3` and mixed `M(D)`. The four z-probes of this same seed give cyclic
lex-smallest reverse hold and cyclic lex-smallest face hold. The four
x-probes give cyclic lex-smallest reverse fail and cyclic lex-smallest
face fail. Those probe-direction readouts are not this y-probe display.
Leftover-empty face fails because leftover of the union is empty at `C`.
Leftover of `M` at `C` is `{e_1, e_3}` and leftover of `M` at `D` is
`{e_1, e_2}`: nonempty and unequal. Leftover of `O` at `C` is `{e_2}` and
leftover of `O` at `D` is `{e_2, e_3}`: nonempty and unequal.
Exist-opposite face of signed `M` fails. Exist-opposite face of signed `O`
holds. Unique signed face fails. Opposite-pair leftover-axis face fails.
Lexicographic face fails. Lex-one oriented face fails. Cyclic lex-largest
face fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover fails at `D` and split fails at `D`. Pair HOLDs at
`D`. Orient at `D` is fail.

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
- It does not replace Orient by lexicographic `o1,o2` orientation.
- It does not replace Orient by nm2orioney lex-one orientation.
- It does not replace Orient by nm2oricyclz cyclic lex-largest orientation.
- It does not replace Orient by opposite-pair leftover-axis orientation.
- It does not replace Orient by unique signed `|O_i|=1` letters.
- It does not replace Orient by unsigned axis units of `Axis(O)`.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not treat split fail as `UNDEFINED`.
- It does not treat empty `O_next` or empty `O_prev` as `UNDEFINED`.
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
- It does not reprint lexicographic `o1,o2` reverse fail face fail as this
  oriented display.
- It does not reprint nm2orioney lex-one reverse hold face fail as this
  oriented display.
- It does not reprint nm2oricyclz cyclic lex-largest reverse fail face fail
  as this oriented display.
- It does not reprint nm2orichy opposite-pair leftover-axis reverse fail
  face fail as this oriented display.
- It does not reprint nm2oridetz unique signed reverse fail face fail as
  this oriented display.
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
two-axis opposite seed process, cyclic next/prev lex-smallest outgoing
determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1`, and
the reverse/face bits from that sign are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; HOLD at `A,B,C`, fail at `D` |
| unique signed `m` and cyclic `(i,o_next,o_prev)` | Theorem 1; singleton `M`; cyclic pair HOLD at `A,B,C`, fail at `D` |
| integer `det(m,o_next,o_prev)` | Theorem 1; `1`, `1`, `1`, fail |
| Orient at `τ` | Theorem 1; `+1`, `+1`, `+1`, fail |
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
| leftover of nm2ax axis-cover HOLD | not this oriented display |
| leftover of nm2ax12 1-in 2-out split HOLD | not this oriented display |
| leftover of lexicographic `o1,o2` | not this oriented display |
| leftover of nm2orioney lex-one | not this oriented display |
| leftover of nm2oricyclz cyclic lex-largest | not this oriented display |
| leftover of nm2orichy opposite-pair leftover-axis | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
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
| empty cyclic slot scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1` on the four y-probes of the two-axis opposite seed, and reverse/face from that sign. |
| V2 | Current main has no landed cyclic-next-prev-lex-smallest-outgoing-determinant reverse/face of timed `M` and `O` on these four y-probes of the two-axis opposite seed. |
| V3 | Orient reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads cyclic next/prev lex-smallest signed outgoing letters of `Axis(m)` at the same `t+1` cut, and reverse HOLDs while cyclic lex-largest reverse fails, while unique signed reverse fails, while lexicographic reverse fails, and while opposite-pair leftover-axis reverse fails, and while lex-one Orient at `C` is `−1`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by lexicographic `o1,o2`, does not replace Orient by nm2orioney
lex-one, does not replace Orient by nm2oricyclz cyclic lex-largest, does
not replace Orient by nm2orichy opposite-pair leftover-axis, does not
replace Orient by nm2oridetz unique signed `|O_i|=1`, does not replace
Orient by nmcover axis-cover, does not replace Orient by nm2ax axis-cover,
does not replace Orient by nm2ax12 1-in 2-out split, does not identify this
display with the 1-axis opposite two-site seed, and does not identify it
with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| lexicographic `o1,o2` | reuse unsigned reverse fail | lexicographic reverse fails (`−1,+1`) while this reverse HOLDs (`+1,+1`); unsigned axis units occupy mixed `O` once | ATTEMPTED |
| nm2orioney lex-one | reuse axis-order signed reverse hold | lex-one reverse HOLDs on `A,B` but `Orient(C)=−1` from `e1<e2<e3`, while cyclic `o_next,o_prev` at `C` gives `+1` | ATTEMPTED |
| nm2oricyclz cyclic lex-largest | reuse cyclic slots with `−e` if both signs | cyclic lex-largest reverse fails (`+1,−1`) because `o_prev(B)=−e_3`; this reverse HOLDs from lex-smallest `+e_3` | ATTEMPTED |
| nm2orichy opposite-pair leftover-axis | reuse leftover-axis reverse fail and face fail | leftover-axis reverse fails from no pair at `A` while this reverse HOLDs; leftover unit is unsigned | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique-signed reverse fail | unique signed reverse fails because `|O ∩ {±e_3}|=2` at `B` while lex-smallest picks `+e_3` and reverse HOLDs | ATTEMPTED |
| nm2ax axis-cover | reuse cover reverse hold and cover face fail on these y-probes | cover does not report the signs `+1,+1`; lexicographic reverse fails on the same cover HOLD | ATTEMPTED |
| nm2ax12 1-in 2-out split | reuse split reverse hold and split face fail | split does not score handedness; unique signed reverse fails on the same split HOLD | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails while this reverse HOLDs; unique signed `O={+e_1,+e_3}` has empty leftover and cyclic Orient `+1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and at `B` is `{e_2,e_3}`, unsigned leftover, not `det(m,o_next,o_prev)` | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and at `B` is `{e_1}`, unsigned leftover | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold of `M` and of `O` | exist-opposite face of signed `O` holds while Orient face fails | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence reverse fails at `A` while this reverse HOLDs; pair-presence face HOLDs while this face fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-smallest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(B,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is `+1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | unsigned Orient at `A` is `−1` while this Orient is `+1`; flipping `m` from `−e_1` to `+e_1` on `O={+e_2,−e_3}` flips Orient from `+1` to `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `D` is 1-in 1-out cover fail | ATTEMPTED |
| empty cyclic slot as `UNDEFINED` | treat missing signed outgoing on `e_next` or `e_prev` as unformed | empty `O_next` or `O_prev` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(B)=2`, `t(D)=3`, mixed `M(D)`, cover face HOLD | different seed; second pair is a new seed, not a formed child; here `t(D)=2` and cover face fails | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe cyclic lex-smallest reverse HOLDs and face HOLDs; this letter is the four y-probes, face fail | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails and face fails; this letter is the four y-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-smallest outgoing determinant orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse hold and face fail on the two-axis opposite seed | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is two disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(B)` sums to `+e_2` while cyclic lex-smallest Orient is `+1` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of Orient with leftover of
`M` alone, missing identification of Orient with leftover-empty fail, missing
identification of Orient with existential opposite of signed locks, missing
identification of Orient with presence of an opposite pair in `O`, missing
identification of Orient with lexicographic `o1,o2`, missing identification
of Orient with nm2orioney lex-one, missing identification of Orient with
nm2oricyclz cyclic lex-largest, missing identification of Orient with
nm2orichy opposite-pair leftover-axis, missing identification of Orient with
nm2oridetz unique signed `|O_i|=1`, missing identification of Orient with
nmcover axis-cover, missing identification of Orient with nm2ax axis-cover,
missing identification of Orient with nm2ax12 1-in 2-out split, missing
identification of this seed with the 1-axis opposite two-site seed, and
missing Record identification of Orient reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
`e_next,e_prev` of `Axis(m)`, lex-smallest signed outgoing letter on each
cyclic slot under `+e < −e`, integer determinant sign, empty cyclic slot as
Orient fail not `UNDEFINED`, split fail as Orient fail not `UNDEFINED`,
four y-probes with seed `A`, second pair as a new seed not a formed child,
and mixed remains a set are declared. No uniqueness of outgoing locks, no
six-neighbor lock union as the scored object, no lock-count clock, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
Orient `hold`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | unique signed incoming letter and cyclic next/prev lex-smallest outgoing letters of `Axis(m)` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports, reverse/face from equal `±1` signs | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out frames. None
is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse hold and face fail are only nm2ax cover reverse
hold and face fail, or nm2ax12 split reverse hold and face fail; leftover of
`M` alone already answers reverse; leftover of `O` alone already answers
reverse; exist-opposite of signed `O` already answers reverse; lexicographic
`o1,o2` already answers handedness; opposite-pair leftover-axis already
answers handedness; unique signed `|O_i|=1` already answers the signed
outgoing plane; nm2orioney lex-one already answers signed outgoing
handedness; nm2oricyclz cyclic lex-largest already answers cyclic slots;
mixed #7188 already reported fail/fail; the second pair is only the formed
child of the 1-axis seed; unique outgoing letters should be required; and
unsigned incoming axis already gives the same signs.

**Answer:** Cover and split HOLD reverse on this member as three-axis
occupation bits. They do not report `Orient(A)=+1`. Lexicographic reverse
fails with `−1,+1` on the same cover HOLD and the same split HOLD, so cover
and split do not score handedness. Unique signed reverse fails because
`|O ∩ {±e_3}|=2` at `B`, while lex-smallest picks `+e_3` and reverse HOLDs.
Opposite-pair leftover-axis reverse fails from no opposite pair at `A`.
Leftover-empty reverse fails while this reverse HOLDs. Leftover of `M`
alone at `A` and at `B` is `{e_2,e_3}`: unsigned leftover, not
`det(m,o_next,o_prev)`. Leftover of `O` alone at `A` and at `B` is `{e_1}`.
Exist-opposite face of signed `O` holds while Orient face fails. Unique
outgoing letters would assign `UNDEFINED` at mixed `O(B)`; this Orient is
`+1`, not `UNDEFINED`. Unsigned incoming axis at `A` is `−1` while signed
`m=−e_1` gives `+1`. Lex-one reverse HOLDs on `A,B` but lex-one Orient at
`C` is `−1` from axis order, while cyclic `det(+e_2,+e_3,+e_1)=+1`. Cyclic
lex-largest reverse fails with `+1,−1` on the same cyclic slots. Mixed
#7188 is a different z-symmetric process with mixed `M`. The second pair is
a new seed, not a formed child: `(0,0,1)` is recorded at tick 0 with lock
`+e_2`. Reverse oriented frame is HOLD iff equal `±1` signs at `A` and at
`B`, not leftover of lexicographic `o1,o2`, not leftover of nm2orioney
lex-one, not leftover of nm2oricyclz cyclic lex-largest, not leftover of
nm2orichy opposite-pair leftover-axis, and not leftover of nm2oridetz
unique signed.

### N8 — cross-cycle echo

nm2ax cover on this two-axis seed reported cover HOLD at `A,B,C`, cover fail
at `D`, reverse hold, and face fail. nm2ax12 1-in 2-out split on the same
seed reported split HOLD at `A,B,C`, split fail at `D`, reverse hold, and
face fail. Lexicographic `o1,o2` on the same y-probes reported Orient
`−1,+1,−1`, fail, reverse fail, and face fail. nm2orichy opposite-pair
leftover-axis on the same y-probes reported Orient fail, `−1`, `−1`, fail,
reverse fail, and face fail. Unique signed `|O_i|=1` on the same y-probes
reported Orient `+1`, fail, fail, fail, reverse fail, and face fail.
nm2orioney lex-one on the same y-probes reported Orient `+1,+1,−1`, fail,
reverse hold, and face fail. Cyclic lex-largest on the same cyclic slots
reported Orient `+1,−1,+1`, fail, reverse fail, and face fail. Leftover
axis reported empty leftover at `A,B,C`, leftover `{e_2}` at `D`, leftover
reverse fail, and leftover face fail. The four z-probes of this same seed
reported cyclic lex-smallest reverse hold and cyclic lex-smallest face
hold. This note is not those displays: it reports cyclic next/prev
lex-smallest outgoing determinant orientation of the 1-in 2-out frame of
`M` and `O` at `τ=t+1` on the two-axis opposite seed, with `t(A)=0`,
`t(B)=1`, `t(C)=1`, and `t(D)=2`, `Orient(A)=+1`, `Orient(B)=+1`,
`Orient(C)=+1`, `Orient(D)=fail`, reverse hold, and face fail. Cover and
split do not score handedness.

**Gate disposition:** PASS for the cyclic-next-prev-lex-smallest-outgoing-determinant `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals lexicographic `o1,o2` HOLD,” “the predicate
equals nm2orioney lex-one HOLD,” “the predicate equals nm2oricyclz cyclic
lex-largest HOLD,” “the predicate equals nm2orichy opposite-pair leftover-axis
HOLD,” “the predicate equals nm2oridetz unique signed HOLD,” “the predicate
equals nmcover axis-cover HOLD,” “the predicate equals nm2ax axis-cover
HOLD,” “the predicate equals nm2ax12 1-in 2-out split HOLD,” “the predicate
equals the 1-axis opposite two-site seed,” “the predicate equals nmunopp
union,” “bits are Admissibility,” “split fail is UNDEFINED,” “empty cyclic
slot is UNDEFINED,” or “face oriented frame holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports split of the pair, reports the unique signed incoming letter and
the cyclic next/prev lex-smallest outgoing letters of `Axis(m)`, reports the
integer determinant and its sign, lists new records in `B_3(0)` between
`t` and `t+1` that meet a probe's six-neighbors, and checks Theorems 1--3.
It also checks that Orient is `+1` at `A`, at `B`, and at `C`, and fail
at `D`, that reverse HOLDs and face fails, that unique signed reverse fails
while this reverse HOLDs, that lexicographic reverse fails while this reverse
HOLDs, that cyclic lex-largest reverse fails while this reverse HOLDs, that
lex-one Orient at `C` is `−1` while this Orient at `C` is `+1`, that split
fail is Orient fail not `UNDEFINED`, that empty cyclic slot is Orient fail
not `UNDEFINED`, that the 1-axis opposite two-site seed is a different
member with `t(D)=3`, that leftover-empty fail is a different predicate,
that leftover of `M` alone and leftover of `O` alone are different objects,
that mixed sets remain sets, that unique-letter Orient is `UNDEFINED` at
mixed `O`, that opposite-pair leftover-axis reverse fails while this reverse
HOLDs, that the construction does not sum, that a formation member from
already-recorded six-neighbor locks is not attached, that the second pair
is a new seed not a formed child, that the z-probes and x-probes of this
seed are not this letter, and that the display is not the two-tick
lock-count clock composition. No runner cache is written.
