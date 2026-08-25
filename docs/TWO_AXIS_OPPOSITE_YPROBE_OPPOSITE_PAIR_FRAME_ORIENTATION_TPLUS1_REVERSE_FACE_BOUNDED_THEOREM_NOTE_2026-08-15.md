---
claim_id: two_axis_opposite_yprobe_opposite_pair_frame_orientation_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Opposite-pair orientation of the 1-in 2-out frame at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_opposite_pair_frame_orientation_tplus1_reverse_face_2026_08_15.py
---

# Opposite-Pair Orientation Of The 1-In 2-Out Frame At t+1 Reverse And Face On Four Y-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** opposite-pair orientation of the 1-in 2-out frame of simultaneous
earliest incoming set `M` and outgoing dual `O` at each probe's `τ=t+1`,
and reverse/face from that sign, on the four y-probes of the two-axis
opposite seed in `B_3(0)={n:n·n<=9}`. Same process and y-probes as nm2ax.
Let `t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)`
is the set of earliest incoming nearest-neighbor steps at `q` using only
records with tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is
the outgoing dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that
`q+e` is formed and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`.
Empty `O` is empty, not `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). Pair HOLDs if and only if `O` contains
some `e` and `−e`. When `M` is singleton `{m}` and `O` contains some `e`
and `−e`, let `o_pair` be that `e` of smallest axis index, leftover axis
`ℓ` the unique Axis not in `{axis(m), axis(e)}`, oriented as the unit
`+ℓ`. `Orient(q)` is the sign of the integer determinant of the 3×3 matrix
with columns `m`, `e`, `+ℓ`. Split HOLD is required. If no opposite pair
in `O`, fail, not `UNDEFINED`. Reverse HOLDs if and only if
`Orient(A)=Orient(B)` both `±1`. Face HOLDs if and only if
`Orient(C)=Orient(D)` both `±1`. Same Orient definition as nm2orichz. This
is not leftover of nm2ax 1-in 2-out split. This is not leftover of
lexicographic o1,o2. This is not leftover of nm2orichz z-probe
opposite-pair. This is not leftover of leftover-of-`M` alone. This is not
leftover of leftover-of-`O` alone. This is not leftover-empty fail of
leftover axis. This is not leftover of nmunopp union. This is not leftover
of nmt2opp `M` frozen at `t`. This is not leftover of nmot2opp two-tick
composition. This is not leftover of nmoutopp untimed eventual-`O`. This
is not leftover of mixed #7188 fail/fail. This is not leftover of the
1-axis opposite two-site seed. This is not leftover of the same-lock
two-site seed. This is not the two-tick lock-count clock composition. The
second pair is a new seed, not a formed child. Uniqueness is not required.
Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_opposite_pair_frame_orientation_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_opposite_pair_frame_orientation_tplus1_reverse_face_2026_08_15.py)

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
Split is cover together with `|Axis(M)|=1`. Pair is presence of some `e`
and `−e` in `O`. The oriented frame is the integer sign of `det(m,e,+ℓ)`
with unique signed incoming letter `m`, opposite-pair unit `e` of smallest
axis index, and leftover unit `+ℓ`. Reverse and face are scored on equal
`±1` signs at the paired probes. Named signs `{+,−}` of locks are a coarser
readout and are not used as the object. A singleton unique outgoing lock
letter is a different readout and is not used as the object. Existential
opposite of signed locks is a different readout and is not used.
Axis-cover without the frame sign is a different readout and is not used.
1-in 2-out split without the opposite-pair frame sign is a different
readout and is not used. Lexicographic unsigned outgoing 2-plane
`(o1,o2)` is a different readout and is not used. Leftover-empty fail of
unsigned leftover axis sets is a different readout and is not used. A
`Z^3` sum of those locks is a different readout and is not used.
Occupancy of sites is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of opposite-pair orientation of the 1-in 2-out frame of M and O at t+1 on the four y-probes of the two-axis opposite seed, Orient fail,-1,-1,fail, reverse fail and face fail from equal +/-1 signs; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_yprobe_opposite_pair_frame_orientation_tplus1_reverse_face
target_blocker_text: "display opposite-pair orientation of the 1-in 2-out frame at t+1 reverse/face on the four y-probes of the two-axis opposite seed, not cover, not split, not lex o1,o2"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep opposite-pair orientation of the 1-in 2-out frame of M and O at t+1 displayed; do not write Orient into Admissibility, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by existential opposite of signed locks, do not replace Orient by lexicographic o1,o2, do not replace Orient by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for opposite-pair orientation of the 1-in 2-out frame of M and O at t+1 on the four y-probes of the two-axis opposite seed and reverse/face from that sign; displayed, not adopted"
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
opposite-pair orientation of the 1-in 2-out frame of `M` and `O` is scored:

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

## Named opposite-pair orientation of the 1-in 2-out frame of `M` and `O` at `τ=t+1`

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

Pair at a probe at the same cut:

```text
pair(q) HOLDs iff O contains some e and −e.
UNDEFINED if O is UNDEFINED. Else fail.
```

Uniqueness of the opposite pair is not required. When several opposite
pairs sit in `O`, the scored pair is the one of smallest axis index.

Opposite-pair oriented frame at the same cut:

```text
When split HOLDs, m is the unique signed letter in M.
If O contains some e and −e, o_pair is that e of smallest axis index.
ℓ is the unique Axis not in {axis(m), axis(e)}, oriented as +ℓ.
Orient(q) = sign of the integer determinant of columns (m, e, +ℓ).
Else fail, not UNDEFINED, if split fails.
If no opposite pair in O, fail, not UNDEFINED.
UNDEFINED if M or O is UNDEFINED.
```

The leftover unit `+ℓ` is the positive basis vector of the unique unused
axis. Unique outgoing letters are not required. A vanishing determinant is
fail. Sign of a nonzero integer determinant is `+1` or `−1`. Split HOLD is
required: pair HOLD with split fail is Orient fail, not `UNDEFINED`.

Reverse opposite-pair frame holds if and only if `Orient(A)=Orient(B)` and
both signs are `±1`. Face opposite-pair frame holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs at `A` and at `B` while `Orient(A)`
is fail. Identifying split reverse with this reverse is refused: split
HOLDs at `A` and at `B` while `Orient(A)` is fail and `Orient(B)=−1`.
Identifying lexicographic `o1,o2` with this Orient is refused:
lexicographic `Orient(A)=−1` and `Orient(B)=+1` while opposite-pair
`Orient(A)` is fail and `Orient(B)=−1`. Identifying leftover-empty fail
with this reverse is refused: leftover-empty fail scores empty leftover as
fail. Identifying a named sign of those locks with reverse or face is
refused: named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, pair, and Orient at `τ=t+1`

On this process the four y-probes form. Compare to leftover axis: leftover
of the union is empty at `A`, `B`, and `C`, leftover `{e_2}` at `D`,
leftover reverse fail and leftover face fail. Compare to nm2ax 1-in 2-out
split: split HOLDs at `A`, `B`, and `C`, fails at `D`, reverse hold and
face fail. Compare to lexicographic `o1,o2`: that readout scores
`Orient(A)=−1` and `Orient(B)=+1` from the unsigned outgoing 2-plane.
Compare to nm2orichz z-probe opposite-pair: that readout on the four
z-probes scores reverse hold and face fail. This display reads the
opposite-pair orientation of those same timed sets on the four y-probes:

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
pair(A) = fail
pair(B) = hold
pair(C) = hold
pair(D) = hold
e(A) = fail
ℓ(A) = fail
det(A) = fail
Orient(A) = fail
e(B) = +e_3
ℓ(B) = +e_2
det(B) = −1
Orient(B) = −1
e(C) = +e_1
ℓ(C) = +e_3
det(C) = −1
Orient(C) = −1
e(D) = +e_1
ℓ(D) = +e_2
det(D) = fail
Orient(D) = fail
```

`A` is a seed at tick 0 with seed letter `−e_1`. Mixed remains a set:
`O(A,τ)` has two outgoing steps and `O(B,τ)` has three outgoing steps.
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
member and do not score that `Orient(A)` is fail. O is not M.

On the 1-axis opposite two-site seed, `B` forms at tick 2 and `D` at tick
3. That is leftover of the first pair. Here both `(0,0,1)` and `(0,1,1)`
are seeds of a second opposite pair on a second axis.

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
Pair fails at `t` at each probe. Orient at `t` is fail, not UNDEFINED.

## Theorem 2 — reverse from opposite-pair frame at `τ`

Reverse opposite-pair frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. `Orient(A)` is fail and `Orient(B)=−1`. Reverse fails. This is HOLD
iff equal `±1` signs, not leftover of nm2ax 1-in 2-out split, not leftover
of lexicographic o1,o2, not leftover-empty fail, and not exist-opposite.

Reverse opposite-pair frame at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Opposite-pair reverse fails because `Orient(A)` is fail. Pair reverse fails
because
pair fails at `A`. Leftover-empty reverse fails because leftover of the
union is empty at `A` and at `B`. Leftover of `M` reverse HOLDs because
leftover of `M` at `A` and at `B` is `{e_2, e_3}`: nonempty and equal.
Leftover of `O` reverse HOLDs because leftover of `O` at `A` and at `B` is
`{e_1}`: nonempty and equal. Exist-opposite reverse of signed `M` holds.
Exist-opposite reverse of signed `O` holds. Lexicographic reverse fails
from opposite signs `−1` and `+1`, a different pair of values than fail
and `−1`. Those leftovers are not this display.

Reverse fails.

## Theorem 3 — face from opposite-pair frame at `τ`

Face opposite-pair frame holds if and only if `Orient(C)=Orient(D)` both
`±1`. `Orient(C)=−1` and `Orient(D)` is fail. Face fails.

Face opposite-pair frame at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Opposite-pair face fails because Orient fails at `D`
from split fail, even though pair HOLDs at `C` and at `D`. Pair face HOLDs
while Orient face fails: split HOLD is required. On the 1-axis opposite
two-site seed, cover face HOLDs while split face fails, and Orient at `D`
is fail, not UNDEFINED. This two-axis member is not leftover of that
1-axis split face fail. The four z-probes of this same seed give
opposite-pair reverse hold and opposite-pair face fail. The four x-probes
give opposite-pair reverse fail and opposite-pair face fail. Those
probe-direction readouts are not this y-probe display. Leftover-empty face
fails because leftover of the union is empty at `C`. Leftover of `M` at
`C` is `{e_1, e_3}` and leftover of `M` at `D` is `{e_1, e_2}`: nonempty
and unequal. Leftover of `O` at `C` is `{e_2}` and leftover of `O` at `D`
is `{e_2, e_3}`: nonempty and unequal. Exist-opposite face of signed `M`
fails. Exist-opposite face of signed `O` holds. Lexicographic face fails
from `Orient(C)=−1` and Orient fail at `D`. Opposite-pair face fails.

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
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the opposite-pair
  frame sign.
- It does not replace Orient by lexicographic `o1,o2`.
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
- It does not reprint nm2ax 1-in 2-out split reverse hold face fail as this
  oriented display.
- It does not reprint lexicographic o1,o2 reverse fail face fail as this
  opposite-pair display.
- It does not reprint nm2orichz z-probe opposite-pair reverse hold face
  fail as this y-probe display.
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
frame of `M` and `O` at `t+1`, and the reverse/face bits from that sign are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; HOLD at `A,B,C`; fail at `D` |
| pair at `τ` | Theorem 1; fail at `A`; HOLD at `B,C,D` |
| unique signed `m`, pair `e`, leftover `+ℓ` | Theorem 1; fail at `A`; `e=+e_3`, `ℓ=+e_2` at `B` |
| integer `det(m,e,+ℓ)` | Theorem 1; `fail,−1,−1,fail` |
| Orient at `τ` | Theorem 1; `fail,−1,−1,fail` |
| reverse from opposite-pair frame at `τ` | Theorem 2; `fail` |
| face from opposite-pair frame at `τ` | Theorem 3; `fail` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this oriented display |
| leftover of exist-opposite HOLD | not this oriented display |
| leftover of nmcover axis-cover HOLD | not this oriented display |
| leftover of nm2ax 1-in 2-out split HOLD | not this oriented display |
| leftover of lexicographic o1,o2 | not this oriented display |
| leftover of nm2orichz z-probe opposite-pair | not this letter |
| y-probe split without opposite-pair Orient | not this letter |
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
| missing opposite pair scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| opposite-pair frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: opposite-pair orientation of the 1-in 2-out frame of `M` and `O` at `t+1` on the four y-probes of the two-axis opposite seed, and reverse/face from that sign. |
| V2 | Current main has no landed opposite-pair-frame reverse/face of timed `M` and `O` on these four y-probes of the two-axis opposite seed. |
| V3 | Orient reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the integer sign of the opposite-pair 1-in 2-out frame of own incoming and own outgoing at the same `t+1` cut, and reverse fails while split reverse HOLDs. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by nmcover axis-cover, does not replace Orient by nm2ax
1-in 2-out split, does not replace Orient by lexicographic `o1,o2`, does
not identify this display with nm2orichz z-probe opposite-pair, does not
identify this display with the 1-axis opposite two-site seed, and does not
identify it with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2ax 1-in 2-out split | reuse split reverse hold and split face fail on these y-probes | split reverse HOLDs while Orient reverse fails: `Orient(A)` is fail | ATTEMPTED |
| lexicographic o1,o2 | reuse sign det(m,o1,o2) with unsigned Axis(O) in axis order | lex `Orient(A)=−1` and `Orient(B)=+1`; opposite-pair `Orient(A)` is fail and `Orient(B)=−1` | ATTEMPTED |
| nm2orichz z-probe opposite-pair | reuse reverse hold and face fail on the four z-probes | z-probe Orient is `−1,−1,+1,−1` with reverse hold; this letter is the four y-probes with reverse fail | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails with Orient reverse, leftover face fails with Orient face, but pair HOLDs at `D` while leftover at `D` is `{e_2}` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and at `B` is `{e_2,e_3}`, nonempty equal, leftover-of-`M` reverse HOLDs while Orient reverse fails | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and at `B` is `{e_1}`, nonempty equal, leftover-of-`O` reverse HOLDs while Orient reverse fails | ATTEMPTED |
| exist-opposite | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `O` holds while Orient reverse fails; exist-opposite face of signed `O` holds while Orient face fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of signed incoming, pair unit, and leftover `+ℓ` | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; pair fails at `A` because no `e` and `−e`, not because mixed | ATTEMPTED |
| missing pair as `UNDEFINED` | treat no opposite pair as unformed | no opposite pair is Orient fail, not UNDEFINED; `A` is formed at tick 0 | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `D` here is 1-in 1-out cover fail with pair HOLD | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(B)=2`, `t(D)=3`, mixed `M(D)` | different seed; second pair is a new seed, not a formed child; here `t(B)=1` and `t(D)=2` | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe opposite-pair reverse HOLDs; this letter is the four y-probes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails at a different `M(A)`; this letter is the four y-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores the opposite-pair frame of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports Orient `fail,−1,−1,fail`, reverse fail, and face fail from opposite-pair | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is two disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `+e_2−e_3` while pair fails | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the opposite-pair frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of Orient with leftover of
`M` alone, missing identification of Orient with leftover-empty fail, missing
identification of Orient with existential opposite of signed locks, missing
identification of Orient with nmcover axis-cover, missing identification of
Orient with nm2ax 1-in 2-out split, missing identification of Orient with
lexicographic `o1,o2`, missing identification of this letter with nm2orichz
z-probe opposite-pair, missing identification of this seed with the 1-axis
opposite two-site seed, and missing Record identification of Orient reverse
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, pair as presence of some `e` and `−e` in `O`,
unique signed `m` when split HOLDs, opposite-pair unit of smallest axis
index, leftover unit `+ℓ`, integer determinant sign, split fail as Orient
fail not `UNDEFINED`, missing opposite pair as Orient fail not
`UNDEFINED`, four y-probes with seed `A`, second pair as a new seed not a
formed child, and mixed remains a set are declared. No uniqueness of
outgoing locks, no six-neighbor lock union as the scored object, no
lock-count clock, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
Orient `fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | signed incoming letter, opposite-pair unit of smallest axis in `O`, leftover `+ℓ` among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports, reverse/face from equal `±1` signs | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out frames. None
is taken here.

### N7 — hostile steelman

**Steelman:** Opposite-pair reverse fail is only leftover-empty fail; split
reverse already answers the three-axis occupation; leftover of `M` alone
already answers reverse; leftover of `O` alone already answers reverse;
exist-opposite of signed `O` already answers reverse; lexicographic
`o1,o2` already answers reverse fail and face fail; the z-probe
opposite-pair already answers this letter; the second pair is only the
formed child `(0,1,1)` of the 1-axis seed; unique outgoing letters should
be required; missing opposite pair at `A` should be `UNDEFINED`; and pair
HOLD at `D` should make Orient HOLD because leftover `+e_2` is unique.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Orient reverse fails because `Orient(A)` is fail and
`Orient(B)=−1`, while split reverse HOLDs because split HOLDs at `A` and at
`B`. Cover reverse HOLDs on this member and does not score missing opposite
pair. Leftover of `M` alone at `A` and at `B` is `{e_2,e_3}`: nonempty
equal, so leftover-of-`M` reverse HOLDs while Orient reverse fails.
Leftover of `O` alone at `A` and at `B` is `{e_1}`: leftover-of-`O`
reverse HOLDs while Orient reverse fails. Exist-opposite reverse of signed
`O` holds while Orient reverse fails. Lexicographic `Orient(A)=−1` from
unsigned `(e_2,e_3)` while opposite-pair `Orient(A)` is fail because
`O(A)` has no `e` and `−e`. The four z-probes score opposite-pair reverse
hold and face fail with ticks `0,1,1,1`; this letter is the four y-probes
with ticks `0,1,1,2` and reverse fail. Unique outgoing letters would
assign `UNDEFINED` at mixed `O(A)`; pair fails at `A` because no opposite
pair, not because mixed. Missing opposite pair is fail, not `UNDEFINED`:
`A` is a seed at tick 0. Pair HOLDs at `D` and leftover unit is `+e_2`,
but split HOLD is required, so Orient at `D` is fail, not `UNDEFINED`.
Reverse opposite-pair frame is HOLD iff equal `±1` signs at `A` and at
`B`, not leftover of nm2ax 1-in 2-out split.

### N8 — cross-cycle echo

nm2ax 1-in 2-out split on this two-axis seed reported split HOLD at `A`,
`B`, and `C`, split fail at `D` from cover fail with leftover `{e_2}`,
reverse hold, and face fail, with `t(B)=1` and `t(D)=2`. Lexicographic
`o1,o2` on these y-probes scores `Orient(A)=−1`, `Orient(B)=+1`, reverse
fail, and face fail. nm2orichz opposite-pair on the four z-probes of this
same seed scores Orient `−1,−1,+1,−1`, reverse hold, and face fail. Leftover
axis reported empty leftover at `A`, `B`, and `C`, leftover `{e_2}` at
`D`, leftover reverse fail, and leftover face fail. This note is not those
displays: it reports opposite-pair orientation of the 1-in 2-out frame of
`M` and `O` at `τ=t+1` on the two-axis opposite seed, with `t(A)=0`,
`t(B)=1`, `t(C)=1`, and `t(D)=2`, `Orient(A)` fail, `Orient(B)=−1`,
`Orient(C)=−1`, `Orient(D)` fail, reverse fail, and face fail. Cover and
split do not score handedness.

**Gate disposition:** PASS for the opposite-pair-frame `t+1` reverse/face
reports above. FAIL / DO NOT SHIP for “the predicate equals the named
sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals nmcover axis-cover HOLD,”
“the predicate equals nm2ax 1-in 2-out split HOLD,” “the predicate equals
lexicographic o1,o2,” “the predicate equals nm2orichz z-probe
opposite-pair,” “the predicate equals the 1-axis opposite two-site seed,”
“the predicate equals nmunopp union,” “bits are Admissibility,” “split
fail is UNDEFINED,” “missing opposite pair is UNDEFINED,” “reverse
opposite-pair frame holds,” or “face opposite-pair frame holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports split of the pair, reports presence of an opposite pair in `O`,
reports the unique signed incoming letter, the opposite-pair unit of
smallest axis index, and the leftover unit `+ℓ`, reports the integer
determinant and its sign, lists new records in `B_3(0)` between `t` and
`t+1` that meet a probe's six-neighbors, and checks Theorems 1--3. It also
checks that Orient is `fail,−1,−1,fail` at `A,B,C,D`, that reverse fails
while cover reverse and split reverse HOLD, that face fails while pair
face HOLDs, that missing opposite pair is Orient fail not `UNDEFINED`,
that split fail is Orient fail not `UNDEFINED`, that the 1-axis opposite
two-site seed is a different member, that leftover-empty fail is a
different object, that leftover of `M` alone and leftover of `O` alone
are different objects, that lexicographic `o1,o2` is a different Orient
at `A` and at `B`, that the four z-probes give opposite-pair reverse hold,
that mixed sets remain sets, that unique-letter Orient is `UNDEFINED` at
mixed `O`, that the construction does not sum, that a formation member
from already-recorded six-neighbor locks is not attached, that the second
pair is a new seed not a formed child, that the z-probes and x-probes of
this seed are not this letter, and that the display is not the two-tick
lock-count clock composition. No runner cache is written.
