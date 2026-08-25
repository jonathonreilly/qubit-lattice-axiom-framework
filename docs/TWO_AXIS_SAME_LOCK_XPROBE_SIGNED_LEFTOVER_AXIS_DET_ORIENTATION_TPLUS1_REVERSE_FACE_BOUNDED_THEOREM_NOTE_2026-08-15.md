---
claim_id: two_axis_same_lock_xprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Signed leftover-axis det orientation at t+1 on the four x-probes of the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_xprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_2026_08_15.py
---

# Signed Leftover-Axis Determinant Orientation At t+1 Reverse And Face On Four X-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** signed leftover-axis determinant orientation of the 1-in 2-out
frame of simultaneous earliest incoming set `M` and outgoing dual `O` at each
probe's `τ=t+1`, and reverse/face from that sign, on the four x-probes of
the two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. Same process and
x-probes as nm2slpx. Orient as nm2orilefz. Let `t(q)` be the formation tick
of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds are
a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the set of
`e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Axis of a defined lock set `S` is `Axis(S)={e_i | some ±e_i in
S}`. Cover HOLDs at `q` if and only if `Axis(M)` intersect `Axis(O)` is
empty and `Axis(M)` union `Axis(O)` equals `{e_1,e_2,e_3}`. Split HOLDs at
`q` if and only if cover HOLDs and `|Axis(M)|=1` (hence `|Axis(O)|=2`).
Split HOLD required. When split HOLDs and `O` contains some `e` and `−e`,
let `e_pair` be that `e` of smallest axis index. Leftover axis `ℓ` is the
unique Axis not in `{axis(m), axis(e_pair)}`. Let `O_ℓ = O ∩ {± unit of
ℓ}`. If `|O_ℓ|≠1`, Orient fails, not `UNDEFINED`. Else let `o_ℓ` be that
signed vector. `Orient(q)` is the sign of the integer determinant of the
3×3 matrix with columns `m`, `e_pair`, `o_ℓ`. If no opposite pair or split
fails, Orient fails, not `UNDEFINED`. Reverse HOLDs if and only if
`Orient(A)=Orient(B)` both `±1`. Face HOLDs if and only if
`Orient(C)=Orient(D)` both `±1`. Cover and split do not score handedness.
This is not leftover of nm2orilefx signed leftover on the two-axis opposite
seed. This is not leftover of nm2orichz unsigned leftover-axis `+ℓ`. This
is not leftover of nm2orionez lex-one signed outgoing letters. This is not
leftover of nm2oridetz unique `|O_i|=1` signed outgoing letters. This is
not leftover of nm2chiralz lexicographic unsigned `o1,o2`. This is not
leftover of nm2slx axis-cover. This is not leftover of nm2sl12 1-in 2-out
split. This is not leftover of leftover-of-`M` alone. This is not leftover
of leftover-of-`O` alone. This is not leftover-empty fail of leftover axis.
This is not leftover of nmunopp union. This is not leftover of nmt2opp `M`
frozen at `t`. This is not leftover of nmot2opp two-tick composition. This
is not leftover of nmoutopp untimed eventual-`O`. This is not leftover of
mixed #7188 fail/fail. This is not leftover of the 1-axis same-lock
two-site seed. This is not leftover of the two-axis opposite seed. The
second pair is a new seed, not a formed child. A is not a seed. Uniqueness
is not required. Mixed remains a set. Displayed, not adopted. Do not write
into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_xprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_xprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_2026_08_15.py)

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
Split is cover together with `|Axis(M)|=1`. The signed leftover-axis
oriented frame is the integer sign of `det(m,e_pair,o_ℓ)` with unique signed
incoming letter `m`, signed exist-opposite pair unit `e_pair` of smallest
axis index in `O`, and the unique signed outgoing vector `o_ℓ` on leftover
axis `ℓ`. Reverse and face are scored on equal `±1` signs at the paired
probes. Named signs `{+,−}` of locks are a coarser readout and are not used
as the object. A singleton unique outgoing lock letter is a different
readout and is not used as the object. Unsigned leftover unit `+ℓ` is a
different readout and is not used. Unique signed letters requiring
`|O_i|=1` are a different readout and are not used. Lex-one signed outgoing
letters are a different readout and are not used. Existential opposite of
signed locks is a different readout and is not used. Axis-cover without the
frame sign is a different readout and is not used. 1-in 2-out split without
the frame sign is a different readout and is not used. Leftover-empty fail
of unsigned leftover axis sets is a different readout and is not used. A
`Z^3` sum of those locks is a different readout and is not used. Occupancy
of sites is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of signed leftover-axis determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four x-probes of the two-axis same-lock seed, Orient at A,B,C,D, reverse fail and face fail from equal +/-1 signs; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_xprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face
target_blocker_text: "display signed leftover-axis determinant orientation of the 1-in 2-out frame reverse/face on the four x-probes of the two-axis same-lock seed, leftover axis with the signed O vector, not unsigned +l, not lex-one, not unique |O_i|=1, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep signed leftover-axis determinant orientation of the 1-in 2-out frame of M and O at t+1 displayed; do not write Orient into Admissibility, do not reduce to unsigned leftover +l, do not reduce to lex-one signed outgoing, do not reduce to unique |O_i|=1, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by presence of an opposite pair in O, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for signed leftover-axis determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four x-probes of the two-axis same-lock seed and reverse/face from that sign; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose signed
leftover-axis orientation of `M` and `O` is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. A is not a seed. Same process and x-probes as
nm2slpx.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. The second pair is a new seed, not
a formed child: `(0,0,1)` locks `+e_2` and `(0,1,1)` locks `+e_2`. Four
sites form at tick 0. This seed is not the nsopp one-axis two-site seed
`{0,(0,1,0)}` with locks `+e_1/−e_1`. This seed is not the 1-axis same-lock
two-site seed with both sites locking `+e_1`. This seed is not the
two-axis opposite seed that would lock the second pair as `+e_2/−e_2`.
This seed is not the nnseed two-site seed `+e_1/+e_2`. This seed is not the
y-axis opposite `±e_2` seed.

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

Signed leftover-axis oriented frame at the same cut:

```text
When split HOLDs and O contains some e and −e,
e_pair is that e of smallest axis index.
leftover axis ℓ is the unique Axis not in {axis(m), axis(e_pair)}.
O_ℓ = O ∩ {± unit of ℓ}.
If |O_ℓ| ≠ 1, Orient fails, not UNDEFINED.
Else o_ℓ is that signed vector.
Orient(q) = sign of the integer determinant of columns (m, e_pair, o_ℓ).
If no opposite pair in O, fail, not UNDEFINED.
If split fails, fail, not UNDEFINED.
UNDEFINED if M or O is UNDEFINED.
```

The opposite-pair unit is the positive lattice unit of the smallest-index
axis on which `O` contains both signs. Unique outgoing letters are not
required. Mixed opposite signs occupy that axis as the pair. The leftover
letter is the signed `O` vector on leftover axis `ℓ`, not the unsigned unit
`+ℓ`. A vanishing determinant is fail. Sign of a nonzero integer
determinant is `+1` or `−1`. Split HOLD required: cover fail or 2-in 1-out
is Orient fail, not UNDEFINED, even if `O` contains an opposite pair.
Missing leftover signed letter `|O_ℓ|≠1` is Orient fail, not UNDEFINED.

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` and both
signs are `±1`. Face oriented frame holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover and split fail reverse here, but they do
not report that signed leftover at `C` is `−e_2` with `Orient(C)=+1` while
unsigned leftover `+ℓ` at `C` is `+e_2` with unsigned Orient `−1`.
Identifying split reverse with this reverse is refused on the same
handedness gap. Identifying leftover-empty fail with this reverse is
refused: leftover-empty fail scores empty leftover as reverse fail, and
does not read `det(m,e_pair,o_ℓ)`. Identifying lexicographic `o1,o2` or
lex-one signed outgoing orientation with this reverse is refused:
lex-one at `B` is `+1` while signed leftover at `B` is `−1`, and lex-one
at `C` is `−1` while signed leftover at `C` is `+1`. Identifying unsigned
leftover-axis `+ℓ` with this letter is refused: unsigned leftover at `C`
is `+e_2` and signed leftover at `C` is `−e_2`. Identifying presence of an
opposite pair in `O` with this face is refused: pair-presence is a boolean
HOLD/fail and does not read the signed leftover vector; on the two-axis
opposite seed, `O(D)` is `{+e_1,−e_1}` so pair-presence face HOLDs, while
here `O(D)` is `{+e_1}` and pair-presence face fails. Identifying a named
sign of those locks with reverse or face is refused: named-sign lettering
lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, pair, signed leftover, and Orient at `τ=t+1`

On this process the four x-probes form. Cover of timed `M` and `O` fails at
`A` and at `D` because leftover axis `{e_2}` is missing from the union.
`|Axis(M)|=1` at each of the four x-probes, so split equals cover on this
member. Compare to leftover axis: leftover of the union is `{e_2}` at `A`
and at `D` and empty at `B` and at `C`, leftover reverse fail and leftover
face fail. Compare to nm2slx cover and nm2sl12 split: both fail reverse
and face on this member. Compare to nm2orichz unsigned leftover `+ℓ`:
unsigned Orient at `C` is `−1` while signed leftover Orient at `C` is
`+1`. Compare to nm2orionez lex-one: lex-one at `B` is `+1` and at `C` is
`−1`. Compare to nm2orilefx: that opposite-seed display has
`O(D)={+e_1,−e_1}` and pair at `D` equal to `+e_1`. This display reads the
signed leftover-axis oriented frame of those same timed sets on the
same-lock seed:

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ) = {−e_3}
M(B, τ) = {+e_1}
M(C, τ) = {+e_1}
M(D, τ) = {−e_3}
O(A, τ) = {+e_1}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {−e_2, +e_3, −e_3}
O(D, τ) = {+e_1}
split(A) = fail
split(B) = hold
split(C) = hold
split(D) = fail
m(A) = −e_3
pair(A) = fail
leftover(A) = fail
det(A) = fail
Orient(A) = fail
m(B) = +e_1
pair(B) = +e_3
leftover(B) = +e_2
det(B) = −1
Orient(B) = −1
m(C) = +e_1
pair(C) = +e_3
leftover(C) = −e_2
det(C) = +1
Orient(C) = +1
m(D) = −e_3
pair(D) = fail
leftover(D) = fail
det(D) = fail
Orient(D) = fail
```

A is not a seed. `A` forms at tick 2 by the incoming step `−e_3`. Mixed
remains a set: `O(B,τ)` has three outgoing steps and `O(C,τ)` has three.
Unique outgoing letters would assign `UNDEFINED` at mixed `O`. Unique
`|O_i|=1` signed outgoing Orient fails at `B` because `|O ∩ {±e_3}|=2`.
Here the opposite pair in `O` is the signed exist-opposite pair of
smallest axis index, leftover axis is the remaining Axis, and leftover
letter is the signed `O` vector on that axis. At `B`, leftover axis is
`e_2` and `O_ℓ={+e_2}`, so `o_ℓ=+e_2` and `det(+e_1,+e_3,+e_2)=−1`. At
`C`, leftover axis is `e_2` and `O_ℓ={−e_2}`, so `o_ℓ=−e_2` and
`det(+e_1,+e_3,−e_2)=+1`. Unsigned leftover `+ℓ` at `C` would keep `+e_2`
and yield `−1`. At `A` there is no opposite pair in `O`, split fails, and
Orient fails, not `UNDEFINED`. At `D` there is no opposite pair in `O`,
leftover axis is not scored, split fails, and Orient fails, not
`UNDEFINED`. Cover and split do not score that `Orient(C)=+1`. O is not M.

On the 1-axis same-lock two-site seed, cover reverse HOLDs on these
x-probes while split reverse fails from 2-in 1-out, and Orient reverse
fails. That is leftover of the first pair. Here both `(0,0,1)` and
`(0,1,1)` are seeds of a second same-lock pair on a second axis. On the
y-probes of this same seed, split HOLDs at `A` while `O(A)` has no
opposite pair, so signed leftover Orient fails at that y-probe `A`; at
y-probe `C`, `|O_ℓ|=2` and Orient fails. On the z-probes of this same
seed, signed leftover reverse fails and face fails. Those probe-direction
readouts are not this x-probe display.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at `A`, `B`, `C`,
and `D`. Split at `t` fails and Orient is fail, not UNDEFINED.

## Theorem 2 — reverse from oriented frame at `τ`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. `Orient(A)=fail` and `Orient(B)=−1`. Reverse fails. This is HOLD iff
equal `±1` signs, not leftover of nm2orichz unsigned leftover-axis `+ℓ`,
not leftover of nm2orionez lex-one, not leftover of nm2slx axis-cover,
not leftover of nm2sl12 1-in 2-out split, not leftover-empty fail, and
not exist-opposite.

Reverse oriented frame at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse fails
because cover fails at `A`. Split reverse fails because split fails at
`A`. Cover and split do not score handedness. Unsigned leftover reverse
also fails, because unsigned leftover at `A` fails with split, but
unsigned leftover at `C` is not this letter. Lex-one reverse fails
because lex-one at `A` fails and lex-one at `B` is `+1`, opposite in sign
to signed leftover at `B`. Leftover-empty reverse fails because leftover
of the union at `B` is empty while leftover at `A` is `{e_2}`. Leftover
of `M` reverse fails because leftover of `M` at `A` is `{e_1, e_2}` and
at `B` is `{e_2, e_3}`: nonempty and unequal. Leftover of `O` reverse
fails because leftover of `O` at `A` is `{e_2, e_3}` and at `B` is
`{e_1}`: nonempty and unequal. Exist-opposite reverse of signed `M`
fails. Exist-opposite reverse of signed `O` fails. Presence of an
opposite pair in `O` fails at `A` and HOLDs at `B`. Those leftovers are
not this display.

Reverse fails.

## Theorem 3 — face from oriented frame at `τ`

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
`Orient(C)=+1` and `Orient(D)=fail`. Face fails.

Face oriented frame at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Opposite-pair oriented face with unsigned leftover
`+ℓ` also fails, but unsigned leftover Orient at `C` is `−1` while
signed leftover Orient at `C` is `+1`. Lex-one face fails because
lex-one at `C` is `−1` and lex-one at `D` fails. Cover and split do not
score handedness. Presence of an opposite pair in `O` HOLDs at `C` and
fails at `D`, so pair-presence face fails with this face, but
pair-presence is a boolean and does not report `Orient(C)=+1`. On the
two-axis opposite seed, pair-presence face HOLDs because `O(D)` contains
`±e_1`. On the 1-axis same-lock two-site seed, cover reverse HOLDs while
split reverse fails from 2-in 1-out; this two-axis member is not leftover
of that 1-axis split reverse fail. The four y-probes of this same seed
give Orient fail at y-probe `A` from no opposite pair in `O` and Orient
fail at y-probe `C` from `|O_ℓ|≠1`. The four z-probes give signed leftover
reverse fail and face fail. Those probe-direction readouts are not this
x-probe display. Leftover-empty face fails because leftover of the union
is empty at `C` and `{e_2}` at `D`. Leftover of `M` at `C` is
`{e_2, e_3}` and leftover of `M` at `D` is `{e_1, e_2}`: nonempty and
unequal. Leftover of `O` at `C` is `{e_1}` and leftover of `O` at `D` is
`{e_2, e_3}`: nonempty and unequal. Exist-opposite face of signed `M`
fails. Exist-opposite face of signed `O` fails. Signed leftover-axis
oriented face fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Split fails at `A` and at `D`. Orient at `A` is fail.
Orient at `C` is `+1`.

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
- It does not replace Orient by lexicographic `o1,o2` orientation.
- It does not replace Orient by lex-one signed outgoing letters.
- It does not replace Orient by unique `|O_i|=1` signed outgoing letters.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not treat split fail as `UNDEFINED`.
- It does not treat `|O_ℓ|≠1` as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace Orient by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nm2slx axis-cover reverse fail face fail as this
  oriented display.
- It does not reprint nm2sl12 1-in 2-out split reverse fail face fail as
  this oriented display.
- It does not reprint nm2orilefx signed leftover on the two-axis opposite
  x-probes as this same-lock member.
- It does not reprint nm2orichz unsigned leftover-axis `+ℓ` as this
  signed leftover letter.
- It does not reprint nm2orionez lex-one reverse fail face hold on
  z-probes as this x-probe display.
- It does not reprint nm2chiralz lexicographic `o1,o2` as this letter.
- It does not reprint the 1-axis same-lock two-site seed as this member.
- It does not reprint the two-axis opposite seed as this member.
- It does not score the y-probes or the z-probes as this letter.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this oriented display.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint the two-tick lock-count clock composition. This is
  not the two-tick lock-count clock composition.
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
two-axis same-lock seed process, signed leftover-axis orientation of the 1-in
2-out frame of `M` and `O` at `t+1`, and the reverse/face bits from that sign
are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis same-lock seed `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; fail at `A,D`, hold at `B,C` |
| unique signed `m`, opposite pair in `O`, signed leftover `o_ℓ` | Theorem 1; pair fail at `A`, signed leftover `+e_2` at `B`, `−e_2` at `C`, pair fail at `D` |
| integer `det(m,e_pair,o_ℓ)` | Theorem 1; fail, `−1`, `+1`, fail |
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
| leftover of nm2slx axis-cover FAIL | not this oriented display |
| leftover of nm2sl12 1-in 2-out split FAIL | not this oriented display |
| leftover of nm2orilefx opposite-seed signed leftover | not this oriented display |
| leftover of nm2orichz unsigned leftover `+ℓ` | not this oriented display |
| leftover of nm2orionez lex-one | not this oriented display |
| leftover of nm2oridetz unique `|O_i|=1` | not this oriented display |
| leftover of nm2chiralz lexicographic `o1,o2` | not this oriented display |
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
| leftover of the 1-axis same-lock two-site seed | not this display |
| leftover of the two-axis opposite seed | not this display |
| split fail scored as `UNDEFINED` | refused; Orient fail |
| `|O_ℓ|≠1` scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: signed leftover-axis determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1` on the four x-probes of the two-axis same-lock seed, leftover axis with the signed `O` vector not unsigned `+ℓ`, and reverse/face from that sign. |
| V2 | Current main has no landed signed leftover-axis-frame reverse/face of timed `M` and `O` on these four x-probes of the two-axis same-lock seed. |
| V3 | Orient reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the integer sign of `det(m,e_pair,o_ℓ)` from a signed leftover `O` vector at the same `t+1` cut, and `Orient(C)=+1` while unsigned leftover `+ℓ` at `C` is `−1` and the opposite seed has pair-presence face HOLD while this member has pair-presence face fail. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by unsigned leftover unit `+ℓ`, does not replace Orient by
nm2orionez lex-one, does not replace Orient by nm2oridetz unique
`|O_i|=1`, does not replace Orient by nm2chiralz lexicographic `o1,o2`,
does not replace Orient by nm2slx axis-cover, does not replace Orient by
nm2sl12 1-in 2-out split, does not identify this display with nm2orilefx,
does not identify this seed with the 1-axis same-lock two-site seed, and
does not identify it with nmunopp union. No global impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2orichz unsigned leftover `+ℓ` | reuse leftover unit `+ℓ` in place of signed `o_ℓ` | unsigned leftover at `C` is `+e_2` with Orient `−1`; signed leftover at `C` is `−e_2` with Orient `+1` | ATTEMPTED |
| nm2orionez lex-one | reuse lex-smallest signed letter per Axis(`O`) | lex-one at `B` is `+1` while signed leftover at `B` is `−1`; lex-one at `C` is `−1` while signed leftover at `C` is `+1` | ATTEMPTED |
| nm2oridetz unique `|O_i|=1` | require a unique signed letter on each Axis(`O`) | mixed `O(B,τ)` has `|O ∩ {±e_3}|=2`, so unique-outgoing Orient fails at `B` while signed leftover Orient is `−1` | ATTEMPTED |
| nm2chiralz lexicographic `o1,o2` | reuse unsigned axis units of Axis(`O`) | unsigned axis units drop the signed leftover `O` vector; at `C` unsigned plane is `(e_2,e_3)` while `o_ℓ=−e_2` | ATTEMPTED |
| nm2slx axis-cover | reuse cover reverse fail and cover face fail on these x-probes | cover does not report `Orient(C)=+1`; Cover and split do not score handedness | ATTEMPTED |
| nm2sl12 1-in 2-out split | reuse split reverse fail and split face fail | split face fails with this face, but split does not read `det(m,e_pair,o_ℓ)` | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails because leftover at `B` is empty; leftover does not read signed `o_ℓ` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_2}` and at `B` is `{e_2,e_3}`, nonempty unequal | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2,e_3}` and at `B` is `{e_1}`, nonempty unequal | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `M` fails and of signed `O` fails; exist-opposite is a cross-probe boolean, not `det(m,e_pair,o_ℓ)` | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence HOLDs at `C` and fails at `D`; on the opposite seed pair-presence face HOLDs because `O(D)={+e_1,−e_1}`; pair-presence does not report `Orient(C)=+1` | ATTEMPTED |
| nm2orilefx opposite-seed signed leftover | reuse opposite-seed x-probe Orient | opposite `O(D)` is `{+e_1,−e_1}` with pair `+e_1`; here `O(D)` is `{+e_1}` and pair fails; opposite z reverse HOLDs while this z reverse fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of signed incoming, pair unit, and signed leftover | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(B,τ)` remains a set; pair is `+e_3` and Orient is `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| no opposite pair as `UNDEFINED` | treat missing `e` and `−e` in `O` as unformed | missing opposite pair is Orient fail, not UNDEFINED; x-probe `A` is the witness | ATTEMPTED |
| `|O_ℓ|≠1` as `UNDEFINED` | treat empty leftover signed letter as unformed | empty leftover signed letter is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis same-lock two-site seed | reuse first-pair x-probe cover reverse hold | different seed; second pair is a new seed, not a formed child; 1-axis cover reverse HOLDs while this reverse fails | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe Orient fails at `A` from no opposite pair in `O` and at `C` from `|O_ℓ|≠1`; this letter is the four x-probes | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe signed leftover reverse fails and face fails; this letter is the four x-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores the signed leftover-axis oriented frame of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports Orient fail, `−1`, `+1`, fail | ATTEMPTED |
| two-axis opposite seed | reuse `+e_1/−e_1` and `+e_2/−e_2` | different seed; this member is two disjoint same-lock pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(B)` sums to `+e_2` while the pair is `+e_3` | ATTEMPTED |
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
identification of Orient with nm2orionez lex-one, missing identification of
Orient with nm2oridetz unique `|O_i|=1`, missing identification of Orient
with nm2chiralz lexicographic `o1,o2`, missing identification of Orient with
nm2slx axis-cover, missing identification of Orient with nm2sl12 1-in 2-out
split, missing identification of this seed with the 1-axis same-lock two-site
seed, missing identification of this seed with the two-axis opposite seed, and
missing Record identification of Orient reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock seed pairs `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs,
smallest-index opposite pair in `O` when present, leftover axis with the
signed `O` vector `o_ℓ` when `|O_ℓ|=1`, integer determinant sign, missing
opposite pair as Orient fail not `UNDEFINED`, split fail as Orient fail not
`UNDEFINED`, `|O_ℓ|≠1` as Orient fail not `UNDEFINED`, four x-probes with
formed-child `A`, second pair as a new seed not a formed child, and mixed
remains a set are declared. No uniqueness of outgoing locks, no
six-neighbor lock union as the scored object, no lock-count clock, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
Orient `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | signed incoming letter, smallest-index opposite pair in `O`, signed leftover `O` vector on leftover axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports, reverse/face from equal `±1` signs | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out frames. None
is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse fail is only cover reverse or only split
reverse; unsigned leftover `+ℓ` already answers handedness because reverse
and face bits agree; lex-one already answers handedness; leftover-empty
fail already answers reverse; leftover of `M` alone already answers
reverse; leftover of `O` alone already answers reverse; exist-opposite of
signed `O` already answers reverse; pair-presence already answers face;
nm2orilefx already displayed the letter on x-probes; the second pair is
only the formed child of the 1-axis seed; unique outgoing letters should be
required; and z-probe signed leftover already displayed the letter.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Orient reverse fails because `Orient(A)=fail` and
`Orient(B)=−1`, while Orient face fails because `Orient(C)=+1` and
`Orient(D)=fail`. Cover and split fail reverse and face on this member and
do not score that signed leftover at `C` is `−e_2` with `Orient(C)=+1`.
Unsigned leftover `+ℓ` at `C` is `+e_2` with unsigned Orient `−1`; the
reverse and face bits happen to agree with this member and still do not
make `+ℓ` the leftover letter. Lex-one at `B` is `+1` and at `C` is `−1`,
opposite to signed leftover at both probes. Presence of an opposite pair
in `O` HOLDs at `C` and fails at `D`; on the two-axis opposite seed
pair-presence face HOLDs because `O(D)={+e_1,−e_1}`. Pair-presence is a
boolean, not `det(m,e_pair,o_ℓ)`. Leftover of `M` alone at `A` is
`{e_1,e_2}` and at `B` is `{e_2,e_3}`: nonempty unequal. Leftover of `O`
alone at `A` is `{e_2,e_3}` and at `B` is `{e_1}`. Exist-opposite reverse
of signed `O` fails with this reverse, but exist-opposite is a cross-probe
boolean, not `det(m,e_pair,o_ℓ)`. Unique outgoing letters would assign
`UNDEFINED` at mixed `O(B)`; unique `|O_i|=1` Orient fails at `B`. The
second pair is a new seed, not a formed child: `(0,0,1)` is recorded at
tick 0 with lock `+e_2`, whereas the 1-axis child forms at tick 1 with
lock `+e_3`. Z-probe signed leftover reverse fails and face fails; this
letter is the four x-probes. nm2orilefx used the opposite seed, where
`O(D)={+e_1,−e_1}` and z reverse HOLDs. Reverse oriented frame is HOLD iff
equal `±1` signs at `A` and at `B`, not leftover of nm2orichz unsigned
leftover-axis `+ℓ`.

### N8 — cross-cycle echo

nm2slx cover on this two-axis same-lock seed reported cover fail at `A`
and at `D`, reverse fail, and face fail. nm2sl12 1-in 2-out split on the
same seed reported split fail at `A` and at `D`, reverse fail, and face
fail. nm2orilefx signed leftover on the two-axis opposite x-probes
reported `O(D)={+e_1,−e_1}`, pair at `D` equal to `+e_1`, reverse fail,
and face fail, with z reverse HOLD. nm2orichz unsigned leftover-axis `+ℓ`
on z-probes reported reverse hold and face fail, using leftover unit `+ℓ`
rather than signed `o_ℓ`. nm2orionez lex-one on z-probes reported reverse
fail and face hold. The four z-probes of this same seed under signed
leftover report reverse fail and face fail. The four y-probes of this same
seed report signed leftover Orient fail at y-probe `A` from no opposite
pair in `O` and Orient fail at y-probe `C` from `|O_ℓ|≠1`. This note is
not those displays: it reports signed leftover-axis orientation of the
1-in 2-out frame of `M` and `O` at `τ=t+1` on the two-axis same-lock seed
x-probes, with `t(A)=2`, `t(B)=1`, `t(C)=3`, and `t(D)=2`,
`Orient(A)=fail`, `Orient(B)=−1`, `Orient(C)=+1`, `Orient(D)=fail`, reverse
fail, and face fail. Cover and split do not score handedness.

**Gate disposition:** PASS for the signed leftover-axis-frame `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals unsigned leftover unit `+ℓ`,” “the predicate
equals nm2orionez lex-one,” “the predicate equals nm2oridetz unique
`|O_i|=1`,” “the predicate equals nm2chiralz lexicographic `o1,o2` HOLD,”
“the predicate equals nm2slx axis-cover FAIL,” “the predicate equals
nm2sl12 1-in 2-out split FAIL,” “the predicate equals nm2orilefx,” “the
predicate equals the 1-axis same-lock two-site seed,” “the predicate
equals the two-axis opposite seed,” “the predicate equals nmunopp union,”
“bits are Admissibility,” “split fail is UNDEFINED,” “no opposite pair is
UNDEFINED,” “`|O_ℓ|≠1` is UNDEFINED,” “reverse oriented frame holds,” or
“face oriented frame holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports split of the pair, reports the unique signed incoming letter, the
smallest-index opposite pair in `O`, and the signed leftover `O` vector
on leftover axis `ℓ`, reports the integer determinant and its sign, lists
new records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that Orient is
fail, `−1`, `+1`, fail at `A,B,C,D`, that reverse fails, that face fails,
that unsigned leftover Orient at `C` is `−1` while signed leftover Orient
at `C` is `+1`, that split fail is Orient fail not `UNDEFINED`, that no
opposite pair in `O` is Orient fail not `UNDEFINED`, that `|O_ℓ|≠1` is
Orient fail not `UNDEFINED`, that the 1-axis same-lock two-site seed is a
different member, that the two-axis opposite seed is a different member,
that leftover-empty fail is a different reverse, that leftover of `M`
alone and leftover of `O` alone are different objects, that mixed sets
remain sets, that unique-letter Orient is `UNDEFINED` at mixed `O`, that
the construction does not sum, that a formation member from already-recorded
six-neighbor locks is not attached, that the second pair is a new seed not
a formed child, that the y-probes and z-probes of this seed are not this
letter, and that the display is not the two-tick lock-count clock
composition. No runner cache is written.
