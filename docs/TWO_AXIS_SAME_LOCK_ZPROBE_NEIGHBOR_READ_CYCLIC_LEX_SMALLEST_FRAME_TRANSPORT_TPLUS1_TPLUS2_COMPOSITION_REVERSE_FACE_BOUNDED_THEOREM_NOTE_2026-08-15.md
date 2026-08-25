---
claim_id: two_axis_same_lock_zprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of cyclic lex-smallest frame transport at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_zprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Cyclic Lex-Smallest Frame Transport Freeze t+1 Versus t+2 Reverse And Face On Four Z-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of cyclic lex-smallest frame transport of `(m,o_next,o_prev)`
of simultaneous earliest incoming set `M` and outgoing dual `O` at each
probe's `τ1=t+1` and `τ2=t+2`, reverse/face from that neighbor-read at
each cut, and composition, on the four z-probes of the two-axis same-lock
seed in `B_3(0)={n:n·n<=9}`. Same process and z-probes as nm2axz.
Transport as nm2sfzfrm. Neighbor-read of that transport at each cut.
`M`, `O`, split as nm2ax12z. Orient as nm2oricyccz (lex-smallest cyclic).
Let `t(q)` be the formation tick of probe `q`. Cuts are local:
`τ1=t+1`, `τ2=t+2`. There is no global T. Do not score τ=t. `M(q,τ)` is the set of earliest incoming
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
likewise. `F(q)=(m,o_next,o_prev)`. `Orient(q)` is the sign of the integer
determinant of the 3×3 matrix with those columns. If split fails, Orient
fails, not `UNDEFINED`. Transport HOLDs at `q` if and only if split HOLDs
at `q`, `Orient(q)` is `±1`, and some formed six-neighbor `r` has split
HOLD, `Orient(r)` `±1`, and the 3×3 integer matrix sending the columns of
`F(q)` to the columns of `F(r)` is a signed permutation with determinant
`Orient(q)*Orient(r)`. If split or Orient fails at `q`, transport fails,
not `UNDEFINED`. Neighbor-read of that transport HOLDs at `q` if and only
if transport HOLDs at `q` and some formed six-neighbor `r` has transport
HOLD. If transport fails at `q`, neighbor-read fails, not `UNDEFINED`.
Reverse HOLDs if and only if neighbor-read HOLDs at `A` and at `B` at
that cut. Face HOLDs if and only if neighbor-read HOLDs at `C` and at
`D` at that cut. Composition HOLDs if and only if neighbor-read at `τ1`
equals neighbor-read at `τ2` at `A,B,C,D`. Neighbor-read of the scalar
Orient sign fails site-locally at `A` and at `C` on this member at both
cuts. Cover and split do not score handedness. This is not leftover of
nm2frmrdslz neighbor-read of cyclic-frame transport at `t+1` alone. This is not leftover of nm2frmrdslt2 neighbor-read of cyclic-frame transport freeze `t+1` versus `t+2` on this same seed. This is not leftover of nm2sfzfrmrdt2 neighbor-read of cyclic lex-smallest frame transport freeze on the three-axis far-face opposite seed. This is not leftover of nm2sfzfrmrd neighbor-read at `t+1` alone. This is not leftover of nm2sfzfrmt2 transport freeze without neighbor-read. This is not leftover of nm2sfzfrm cyclic lex-smallest frame transport without neighbor-read. This
is not leftover of nm2simt2z simultaneous `M` and `O` freeze. This is not
leftover of nm2cycfrmsl cyclic-frame transport reverse fail whose sending
inspects a signed permutation. This is not leftover of nm2cycfrmz cyclic-frame
transport. This is not leftover of equal transport bits including
fail=fail. This is not leftover of scalar neighbor-read of Orient. This
is not leftover of a unique nonnegative permutation sending. This is not
leftover of nm2oricyccz cyclic lex-smallest Orient reverse/face. This is
not leftover of nm2oricyclslz lex-largest cyclic next/prev. This is not
leftover of nm2oricyclz cyclic next/prev on the opposite seed. This is not
leftover of nm2orionez lex-one signed outgoing orientation. This is not
leftover of nm2slz axis-cover. This is not leftover of nm2chiralz
lexicographic unsigned `o1,o2` orientation. This is not leftover of
nm2oridetz unique signed outgoing letters. This is not leftover of
nm2orichz opposite-pair leftover-axis orientation. This is not leftover of
nm2axz axis-cover. This is not leftover of nm2ax12z 1-in 2-out split. This
is not leftover of leftover-of-`M` alone. This is not leftover of
leftover-of-`O` alone. This is not leftover-empty fail of leftover axis.
This is not leftover of nmunopp union. This is not leftover of nmt2opp `M`
frozen at `t`. This is not leftover of nmot2opp two-tick composition. This
is not leftover of nmoutopp untimed eventual-`O`. This is not leftover of
mixed #7188 fail/fail. This is not leftover of the 1-axis same-lock
two-site seed. Neither pair is opposite. The second pair is a new seed,
not a formed child. Uniqueness is not required. Mixed remains a set.
Occupancy of sites is not used. This display does not use occupancy. A
six-neighbor star is not the letter. Displayed, not adopted. Do not write
into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_zprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_zprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

No runner cache is written.

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cuts
`τ1=t+1` and `τ2=t+2`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev
lex-smallest oriented frame is the integer sign of `det(m,o_next,o_prev)`
with unique signed incoming letter `m` and the lex-smallest signed outgoing
letter on the two axes cyclic from `Axis(M)` under `+e < −e`. `F` is those
three columns when split HOLDs. Transport asks whether some formed
six-neighbor carries a frame related by a signed permutation of
determinant `Orient(q)*Orient(r)`. Neighbor-read of that transport HOLD
bit asks whether some formed six-neighbor itself has transport HOLD.
Reverse and face are scored on neighbor-read HOLD at the paired probes.
Named signs `{+,−}` of locks are a
coarser readout and are not used as the object. A singleton unique
outgoing lock letter is a different readout and are not used as the object.
Unsigned axis units of `Axis(O)` are a different readout and are not used.
Lex-largest cyclic next/prev is a different readout and is not used.
Unique signed letters requiring `|O_i|=1` are a different readout and are
not used. Opposite-pair leftover-axis orientation is a different readout
and is not used. Existential opposite of signed locks is a different
readout and is not used. Axis-cover without the frame is a different
readout and is not used. 1-in 2-out split without the frame is a different
readout and is not used. Orient reverse/face without transport is a
different readout and is not used. Neighbor-read of the scalar Orient sign
is a different readout and is not used. Equal transport bits including
fail=fail is a different readout and is not used. A unique nonnegative
permutation sending is a different readout and is not used. Leftover-empty
fail of unsigned leftover axis sets is a different readout and is not used.
A `Z^3` sum of those locks is a different readout and is not used. A
six-neighbor star is not the letter. O is not M.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of cyclic lex-smallest frame transport of (m,o_next,o_prev) of M and O at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, neighbor-read fail at A from transport fail, neighbor-read HOLD at B,C,D at each cut, reverse fail and face hold at each cut, composition hold; uniqueness of the matching neighbor is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_zprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display neighbor-read of cyclic lex-smallest frame transport freeze t+1 versus t+2 reverse/face composition on the four z-probes of the two-axis same-lock seed, not leftover of nm2frmrdslt2, not leftover of nm2sfzfrmrdt2, not leftover of nm2frmrdslz t+1 alone, not leftover of nm2simt2z, not leftover of nm2cycfrmsl sending, not equal transport bit including fail, not scalar neighbor-read of Orient, not unique nonnegative sending, not leftover-axis, not lex-one e1<e2<e3, not unique |O_i|=1, not unsigned axis units, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of cyclic lex-smallest frame transport of (m,o_next,o_prev) of M and O at t+1 versus t+2 displayed; do not write neighbor-read into Admissibility, do not reduce to nm2frmrdslt2, do not reduce to nm2sfzfrmrdt2, do not reduce to nm2sfzfrmrd t+1 alone, do not reduce to nm2sfzfrmt2, do not reduce to nm2frmrdslz t+1 alone, do not reduce to nm2simt2z M-and-O freeze, do not reduce to nm2cycfrmsl sending, do not reduce to equal transport bit including fail, do not reduce to scalar neighbor-read of Orient, do not reduce to unique nonnegative permutation sending, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-largest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace neighbor-read by unique outgoing letters, do not replace neighbor-read by existential opposite of signed locks, do not replace neighbor-read by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of cyclic lex-smallest frame transport of (m,o_next,o_prev) of M and O at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition; displayed, not adopted"
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
neighbor-read of cyclic lex-smallest frame transport of `F=(m,o_next,o_prev)` of `M`
and `O` is scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the second same-lock pair. Same process and
z-probes as nm2axz.

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

## Named cyclic lex-smallest frame `F` and transport at `τ1` and `τ2`

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
replace `O` by `M`. It does not wait for a global later T. O is not M.

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

Oriented frame and transport at the same cut:

```text
When split HOLDs, m is the unique signed letter in M.
i in {1,2,3} is the axis index of m.
e_next = e_{i+1} with 3+1 → 1.
e_prev = e_{i-1} with 1−1 → 3.
O_next = O ∩ {±e_next}, O_prev = O ∩ {±e_prev}.
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e. o_next is the lex-smallest vector in O_next
(hence +e if both signs). o_prev likewise.
F(q) = (m, o_next, o_prev).
Orient(q) = sign of the integer determinant of columns F(q).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
Transport(q) HOLDs iff split HOLDs at q, Orient(q) is ±1,
and some formed six-neighbor r has split HOLD, Orient(r) ±1,
and the 3×3 integer matrix P sending the columns of F(q) to
the columns of F(r) (F(r)=F(q)P) is a signed permutation
with det(P) = Orient(q)*Orient(r).
If split or Orient fails at q, transport fails, not UNDEFINED.
Uniqueness of r is not required.

Neighbor-read HOLDs at q iff transport(q) HOLDs
and some formed 6-NN r has transport(r) HOLD.
If transport fails at q, neighbor-read fails, not UNDEFINED.
UNDEFINED if transport is UNDEFINED.
Uniqueness of r is not required.
```

Neighbor-read of the scalar Orient sign HOLDs at `q` if and only if
`Orient(q)` is `±1` and some formed six-neighbor has the same sign. That
is a different object: it fails at `A` and at `C` on this member while
neighbor-read of transport HOLDs at `B`, `C`, and `D`. A unique
nonnegative permutation sending is a different object: it HOLDs at `D`
and fails at `A`, `B`, and `C`, so unique-nonnegative face fails. Equal transport bits including fail=fail is a
different object: at `(0,-1,1)` transport fails and a formed
six-neighbor also fails, so equal-bit HOLDs while neighbor-read fails.

The outgoing pair is signed and cyclic from `Axis(M)`, not from axis-order
`e1<e2<e3`. Mixed opposite signs on one cyclic axis make `|O_next|=2` or
`|O_prev|=2`; lex-smallest still picks `+e`, so Orient is defined when split
HOLDs. Unique outgoing letters of the whole set `O` are not required: mixed
`O` remains a set, and unique-letter readout of mixed `O` is `UNDEFINED`
while this Orient is a sign or fail. Empty cyclic side is Orient fail, not
`UNDEFINED`. A vanishing determinant is fail. Sign of a nonzero integer
determinant is `+1` or `−1`. Split HOLD required: 2-in 1-out is Orient
fail, not UNDEFINED. If unique `m` exists, `i`, `o_next`, and `o_prev` may
still be reported when split fails; Orient and transport are then fail, not
those vectors. Formed six-neighbors are sites already recorded in `B_3(0)`
that differ from `q` by one nearest-neighbor step. That neighbor list is
not a scored star letter.

Reverse neighbor-read of cyclic lex-smallest frame transport at a cut holds if and only if
neighbor-read HOLDs at `A` and at `B` at that cut. Face neighbor-read of
cyclic-frame transport at a cut holds if and only if neighbor-read HOLDs
at `C` and at `D` at that cut. Either side `UNDEFINED` is `UNDEFINED`. Else
if both sides HOLD, reverse or face HOLDs. Else fail.

Composition holds if and only if neighbor-read at `τ1` equals neighbor-read
at `τ2` at each of `A,B,C,D`. Either side `UNDEFINED` is `UNDEFINED`. Else if
the four neighbor-read bits agree across the two cuts, composition HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover reverse fails from overlapping `e_2` at
`A` and cover face HOLDs, while transport HOLDs at `C` and at `D`. Identifying
split reverse with this reverse is refused: split reverse fails from
split fail at `A` and split face HOLDs, while transport HOLDs at `C`
and at `D`. Identifying leftover-empty fail with this reverse is
refused: leftover-empty fail scores empty leftover as reverse fail and
face fail, while this face HOLDs. Identifying lexicographic unsigned `o1,o2`
with this reverse is refused: unsigned reverse fails and unsigned face
HOLDs with `+1,+1`, while this reverse fails and this face HOLDs, but
unsigned Orient at `C` is `+1` while cyclic Orient at `C` is `−1`. Identifying
lex-one signed axis-order letters with this reverse is refused: lex-one
signs happen to match cyclic lex-smallest signs on this member at
`B,C,D`, while the letter is cyclic next/prev of `Axis(M)`; on unique
signed `O={+e_1,+e_3}` with `m=+e_2`, cyclic Orient is `+1` and lex-one
Orient is `−1`. Identifying unique signed `|O_i|=1` with this reverse is
refused: unique signed reverse fails and face fails because mixed
opposite pairs occupy `O`. Identifying opposite-pair leftover-axis
orientation with this reverse is refused: leftover-axis reverse fails and
face fails, while this face HOLDs. Identifying nm2oricyccz opposite-seed
Orient reverse hold and face hold with this reverse is refused: nm2oricyccz
has split HOLD at `A` and `Orient(A)=+1` equal to `Orient(B)=+1`; here split
fails at `A` and transport at `A` is fail. Identifying nm2oricyclslz
lex-largest cyclic Orient with this reverse is refused: lex-largest Orient
at `B` is `−1` while lex-smallest Orient at `B` is `+1`. Identifying
nm2oricyccz Orient reverse/face on this same-lock seed with this reverse
is refused: Orient reverse fails and Orient face HOLDs with signs
`fail,+1,−1,−1`, matching these reverse/face bits, while transport at `B`
is hold and Orient at `B` is `+1`, and transport at `C` is hold while
Orient at `C` is `−1`. Identifying nm2slz axis-cover with this reverse is
refused: cover does not report the signed frame or the sending matrix.
Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, `i`, cyclic pair, Orient, transport, and neighbor-read at `τ1` and `τ2`

On this process the four z-probes form. Compare to leftover axis: that
leftover reports empty leftover at each probe and leftover reverse fail
and leftover face fail. Compare to nm2slz axis-cover: cover fails at `A`
from overlapping `e_2` and HOLDs at `B`, `C`, and `D`, so cover reverse
fails and cover face HOLDs. Compare to nm2oricyccz cyclic next/prev
lex-smallest on the two-axis opposite seed: that member has split HOLD at
`A`, `O(A,τ)={+e_1, −e_1, +e_3}` missing the partner letter,
`Orient(A)=+1`, reverse HOLDs from equal `+1` signs, and face HOLDs.
Compare to nm2oricyclslz lex-largest on this same-lock member: reverse
fails and face HOLDs with signs `fail,−1,+1,+1`. Compare to nm2orionez
lex-one on this same-lock member: reverse fails and face HOLDs with signs
`fail,+1,−1,−1`. Compare to nm2axz cover and nm2ax12z split on the opposite
seed: both HOLD reverse and face there. Compare to nm2chiralz lexicographic
unsigned `o1,o2` orientation on this same-lock member: reverse fails and
face HOLDs with unsigned signs `fail,+1,+1,+1`. Compare to nm2oridetz
unique signed outgoing letters: reverse fails and face fails because
`|O_i|≠1`. Compare to nm2orichz opposite-pair leftover-axis orientation:
reverse fails and face fails on this member. This display reads the
neighbor-read of cyclic lex-smallest frame transport of `(m,o_next,o_prev)` of those
same timed sets:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=1
M(A, τ1) = {+e_2}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_3}
M(D, τ1) = {+e_1}
O(A, τ1) = {+e_1, −e_1, +e_2, +e_3}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {+e_1, −e_1, −e_2}
O(D, τ1) = {−e_2, +e_3, −e_3}
split(A, τ1) = fail
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = hold
i(A, τ1) = 2
o_next(A, τ1) = +e_3
o_prev(A, τ1) = +e_1
det(A, τ1) = fail
Orient(A, τ1) = fail
transport(A, τ1) = fail
neighbor-read(A, τ1) = fail
scalar neighbor-read(A, τ1) = fail
i(B, τ1) = 1
o_next(B, τ1) = +e_2
o_prev(B, τ1) = +e_3
det(B, τ1) = 1
Orient(B, τ1) = +1
transport(B, τ1) = hold
neighbor-read(B, τ1) = hold
scalar neighbor-read(B, τ1) = hold
read-witness(B, τ1) = (0, 1, 1)
i(C, τ1) = 3
o_next(C, τ1) = +e_1
o_prev(C, τ1) = −e_2
det(C, τ1) = -1
Orient(C, τ1) = −1
transport(C, τ1) = hold
neighbor-read(C, τ1) = hold
scalar neighbor-read(C, τ1) = fail
read-witness(C, τ1) = (0, 1, 2)
i(D, τ1) = 1
o_next(D, τ1) = −e_2
o_prev(D, τ1) = +e_3
det(D, τ1) = -1
Orient(D, τ1) = −1
transport(D, τ1) = hold
neighbor-read(D, τ1) = hold
scalar neighbor-read(D, τ1) = hold
read-witness(D, τ1) = (1, 1, 1)
M(A, τ2) = {+e_2}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_3}
M(D, τ2) = {+e_1}
O(A, τ2) = {+e_1, −e_1, +e_2, +e_3}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {+e_1, −e_1, −e_2}
O(D, τ2) = {−e_2, +e_3, −e_3}
Orient(A, τ2) = fail
Orient(B, τ2) = +1
Orient(C, τ2) = −1
Orient(D, τ2) = −1
transport(A, τ2) = fail
transport(B, τ2) = hold
transport(C, τ2) = hold
transport(D, τ2) = hold
neighbor-read(A, τ2) = fail
neighbor-read(B, τ2) = hold
neighbor-read(C, τ2) = hold
neighbor-read(D, τ2) = hold
scalar neighbor-read(A, τ2) = fail
scalar neighbor-read(B, τ2) = hold
scalar neighbor-read(C, τ2) = fail
scalar neighbor-read(D, τ2) = hold
read-witness(B, τ2) = (0, 1, 1)
read-witness(C, τ2) = (0, 1, 2)
read-witness(D, τ2) = (1, 1, 1)
```

`A` is a seed at tick 0 with seed letter `+e_2`. The partner of that pair,
`(0,1,1)`, is also a seed at tick 0 with seed letter `+e_2`. Mixed remains
a set: `O(A,τ)` has four outgoing steps and `O(D,τ)` has three outgoing
steps. Unique outgoing letters would assign `UNDEFINED` at mixed `O`.
Unique signed `|O_i|=1` fails at each probe: `O(A)` has both `±e_1`, `O(B)`
has both `±e_3`, `O(C)` has both `±e_1`, and `O(D)` has both `±e_3`. At
`A`, unique `m` still gives `i=2`, `o_next=+e_3`, and `o_prev=+e_1`, but
split fails from overlapping `e_2` in `Axis(O)`, so Orient fails and
transport fails, not `UNDEFINED`. Split HOLD is required. `M` is a
singleton at each probe, so the unique signed `m` exists. Cover and split
fail at `A` from overlapping `e_2` and HOLD at `B`, `C`, and `D`; they do
not score that transport HOLDs at `C` and at `D`. Unsigned axis-order
2-plane at `C` is `(e_1,e_2)` and lexicographic Orient at `C` is `+1`,
while cyclic Orient at `C` is `−1`. Lex-one signed axis-order pair at `B`
is `(+e_2,+e_3)` with Orient `+1`, matching cyclic lex-smallest at `B`;
lex-one at `C` is `(+e_1,−e_2)` matching cyclic at `C`. On
`m=+e_2` and `O={+e_1,+e_3}` cyclic columns are `(+e_3,+e_1)` with Orient
`+1` while lex-one columns are `(+e_1,+e_3)` with Orient `−1`. Opposite-pair
leftover-axis at `D` is pair `+e_3` leftover `−e_2` with Orient `+1`, while
cyclic Orient at `D` is `−1`. The same-lock partner letter `+e_2` is
already in `O(A)` at formation tick `t` itself: `O(A,t)={+e_2}`. O is not M.

`F(B)=(+e_1,+e_2,+e_3)` and `F(D)=(+e_1,−e_2,+e_3)`. The integer matrix
sending the columns of `F(B)` to the columns of `F(D)` is the signed
permutation with columns `(+e_1,−e_2,+e_3)` and determinant `−1`, equal
to `Orient(B)*Orient(D)`. `D` is a formed six-neighbor of `B`, so
transport HOLDs at `B`. Transport at `C` HOLDs by the formed six-neighbor
`(0,1,2)`, which is not among the new records at `t(C)+1`. Transport at
`A` fails because split fails at `A`, even though several formed
six-neighbors of `A` themselves have split HOLD.

On the 1-axis same-lock two-site seed, `A=(0,0,1)` is a formed child at
tick 1 locking `+e_3`, and `C` is 2-in 1-out, so split fails at `C` and
Orient at `C` is fail, not UNDEFINED. That is leftover of the first pair.
Here both `(0,0,1)` and `(0,1,1)` are seeds of a second same-lock pair on a
second axis. On the y-probes of this same seed, split HOLDs at `A` and
`O(A)={+e_2,−e_3}` has nonempty cyclic sides, so cyclic Orient at that
y-probe is `−1`, lexicographic unsigned `o1,o2` there is `+1`, and
opposite-pair leftover-axis Orient there fails from no opposite pair in
`O`. Y-probe reverse fails (`−1,+1`) and y-face fails; this z-probe reverse
fails and this z-face HOLDs.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. The partner seed of
`A` is already recorded at tick 0, so it is not among those new records:

```text
new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)
new 6-NN of A at t(A)+2: (0, -1, 1)
new 6-NN of B at t(B)+2: none
new 6-NN of C at t(C)+2: none
new 6-NN of D at t(D)+2: none
transport witnesses of B include (1, 0, 1)
transport witnesses of C include (0, 1, 2)
transport witnesses of D include (1, 1, 1)
read-witness(B, τ1) = (0, 1, 1)
read-witness(C, τ1) = (0, 1, 2)
read-witness(D, τ1) = (1, 1, 1)
read-witness(B, τ2) = (0, 1, 1)
read-witness(C, τ2) = (0, 1, 2)
read-witness(D, τ2) = (1, 1, 1)
```

`M` is frozen from `t` to `t+1` and from `t+1` to `t+2`. At `t`, `O(A)={+e_2}`
and `O` is empty at `B`, at `C`, and at `D`; split fails at each probe, and
Orient is fail, not UNDEFINED. Do not score `τ=t`. The child `(0,-1,1)` of
`A` forms at `t(A)+2` locking `+e_3` and does not enter `O(A,τ2)`: `O` at
`τ2` equals `O` at `τ1` at each of the four z-probes. Neighbor-read bits at
`τ2` equal the bits at `τ1`. This is the first display of cyclic lex-smallest frame neighbor-read freeze on two-axis same-lock z, including those bits at `t+2`. It is not leftover of nm2frmrdslz at `t+1` alone. It is not leftover of nm2frmrdslt2 cyclic-frame neighbor-read freeze on this seed. It is not leftover of nm2sfzfrmrdt2 on the three-axis far-face opposite seed.

## Theorem 2 — reverse and face from neighbor-read of cyclic lex-smallest frame transport at `τ1` and `τ2`

Reverse neighbor-read of cyclic lex-smallest frame transport at a cut holds if and only if
neighbor-read HOLDs at `A` and at `B` at that cut. At `τ1`,
`neighbor-read(A)=fail` and `neighbor-read(B)=hold`. Reverse fails. At
`τ2` the same bits HOLD/fail, so reverse fails again. This is HOLD iff both
neighbor-reads HOLD, not leftover of nm2frmrdslz at `t+1` alone, not leftover
of nm2simt2z, not leftover of nm2cycfrmsl cyclic-frame transport
sending, not leftover of nm2cycfrmz cyclic-frame transport, not leftover
of equal transport bits including fail=fail, not leftover of scalar
neighbor-read, not leftover of a unique nonnegative permutation sending,
not leftover of nm2oricyccz cyclic next/prev, not leftover of
nm2oricyclslz lex-largest, not leftover of nm2orionez lex-one, not leftover
of nm2slz axis-cover, not leftover of nm2chiralz lexicographic unsigned
`o1,o2`, not leftover of nm2oridetz unique signed outgoing letters, not
leftover of nm2orichz opposite-pair leftover-axis, not leftover of nm2axz
axis-cover, not leftover of nm2ax12z 1-in 2-out split, not leftover-empty
fail, and not exist-opposite.

Reverse neighbor-read of cyclic lex-smallest frame transport at τ1: fail
Reverse neighbor-read of cyclic lex-smallest frame transport at τ2: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse fails
because cover fails at `A` from overlapping `e_2`. Split reverse fails
because split fails at `A`. Cover and split do not score handedness.
Orient reverse fails because `Orient(A)` is fail and `Orient(B)=+1`. Those
Orient reverse bits match these transport reverse bits on this member
while the object differs: transport at `B` is hold, not the sign `+1`.
Lexicographic unsigned reverse fails because unsigned Orient at `A` is
fail and at `B` is `+1`. Lex-one signed reverse fails because lex-one
Orient at `A` is fail and at `B` is `+1`. Unique signed reverse fails
because both unique signed signs fail. Opposite-pair leftover-axis reverse
fails because that Orient at `A` is fail. Leftover-empty reverse fails
because leftover of the union is empty at `A` and at `B`. Leftover of `M`
reverse fails because leftover of `M` at `A` is `{e_1, e_3}` and at `B` is
`{e_2, e_3}`: nonempty and unequal. Leftover of `O` reverse fails because
leftover of `O` at `A` is empty. Exist-opposite reverse of signed `M` fails.
Exist-opposite reverse of signed `O` holds. Presence of an opposite pair
in `O` at `A` and at `B` HOLDs. nm2oricyccz reverse HOLDs from equal `+1`
signs with split HOLD at `A`. Those leftovers are not this display.

Reverse fails at both cuts.

Face neighbor-read of cyclic lex-smallest frame transport at a cut holds if and only if
neighbor-read HOLDs at `C` and at `D` at that cut. At `τ1`,
`neighbor-read(C)=hold` and `neighbor-read(D)=hold`. Face HOLDs. At `τ2`
the same bits HOLD, so face HOLDs again.

Face neighbor-read of cyclic lex-smallest frame transport at τ1: hold
Face neighbor-read of cyclic lex-smallest frame transport at τ2: hold

## Theorem 3 — composition of neighbor-read of cyclic lex-smallest frame transport

Composition of neighbor-read of cyclic lex-smallest frame transport holds if and only
if the four neighbor-read bits at `τ1` equal the four neighbor-read bits
at `τ2`. They do: fail, hold, hold, hold at each cut. Composition HOLDs.
This is not leftover of nm2frmrdslz at `t+1` alone: that letter does not
score `τ2`. This is not leftover of nm2frmrdslt2 neighbor-read of cyclic-frame transport freeze: that letter inspects left-action `T` of cyclic-frame transport, not `F(r)=F(q)P` of nm2sfzfrm. This is not leftover of nm2sfzfrmrdt2 on the three-axis far-face opposite seed. This is not leftover of nm2simt2z `M` and `O` freeze: `M` and
`O` also freeze here, but composition scores neighbor-read equality, not
the sets. Reverse/face bit composition also HOLDs because reverse fails at
both cuts and face HOLDs at both cuts; that is leftover of pairing the
two reverse/face reports, not the four-site neighbor-read equality.
Composition of neighbor-read at `t` versus `t+1` fails: all four
neighbor-reads fail at `t`, while at `t+1` only `A` fails. Do not score
`τ=t`.

Composition of neighbor-read of cyclic lex-smallest frame transport: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face HOLDs because cover HOLDs at `C` and at `D`. Split face HOLDs
because split HOLDs at `C` and at `D`. Cyclic signed Orient face HOLDs
because both signs are `−1`. Transport face HOLDs because both transport
bits HOLD. Those Orient signs are not these transport bits: Orient at `C`
is `−1` while transport at `C` is hold. Lexicographic unsigned face HOLDs
because both unsigned signs are `+1`; those columns are not these columns.
Lex-one signed face HOLDs because both lex-one signs are `−1`; those signs
are not these transport bits. Unique signed face fails because neither
unique signed sign is `±1`. Opposite-pair leftover-axis face fails because
those signs are `−1` and `+1`. Cover and split do not score handedness.
Presence of an opposite pair in `O` HOLDs at `C` and at `D`, so
pair-presence face HOLDs while this face also HOLDs from a different
object: signed-permutation transport of cyclic lex-smallest columns, not
pair presence. On the 1-axis same-lock two-site seed, cover face HOLDs
while split face fails at `C` from 2-in 1-out, and Orient at `C` is fail,
not UNDEFINED. This two-axis member is not leftover of that 1-axis split
face fail. The four y-probes of this same seed give cyclic Orient `−1` at
`A` and Orient fail at `D` from split fail, so oriented y-face fails while
this z-face HOLDs. The four x-probes give oriented reverse fail and
oriented face fail. Those probe-direction readouts are not this z-probe
display. Leftover-empty face fails because leftover of the union is empty
at `C` and at `D`. Leftover of `M` at `C` is `{e_1, e_2}` and leftover of
`M` at `D` is `{e_2, e_3}`: nonempty and unequal. Leftover of `O` at `C`
is `{e_3}` and leftover of `O` at `D` is `{e_1}`: nonempty and unequal.
Exist-opposite face of signed `M` fails. Exist-opposite face of signed `O`
fails. Cyclic lex-smallest frame transport face HOLDs. nm2oricyccz face also HOLDs with
`−1,−1` on the opposite seed; that is leftover of a different seed, not
this same-lock member.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover reverse fails from overlapping axes at `A`. Cover
HOLDs at `D` and split HOLDs at `D`. Orient at `D` is `−1` from cyclic
`(−e_2,+e_3)` even though `|O ∩ {±e_3}|=2`. Orient at `A` is fail because
split fails, not because `O` is unformed. Transport at `A` is fail because
split fails at `A`, not `UNDEFINED`.

Face HOLDs.

## What this note does not claim

- It does not replace neighbor-read of transport by nm2cycfrmz signed-permutation sending.
- It does not replace neighbor-read by equal transport bits including fail=fail.
- It does not replace neighbor-read of transport by neighbor-read of the scalar Orient sign.
- It does not replace neighbor-read of transport by a unique nonnegative permutation sending.
- It does not require a unique formed six-neighbor witness.
- It does not reprint nm2frmrdslz neighbor-read reverse fail face hold at `t+1` as this freeze.
- It does not reprint nm2frmrdslt2 neighbor-read of cyclic-frame transport freeze as this letter.
- It does not reprint nm2sfzfrmrdt2 three-axis far-face opposite neighbor-read freeze as this seed.
- It does not reprint nm2sfzfrmrd neighbor-read at `t+1` alone as this freeze.
- It does not reprint nm2sfzfrmt2 transport freeze without neighbor-read as this letter.
- It does not reprint nm2sfzfrm cyclic lex-smallest frame transport without neighbor-read as this letter.
- It does not reprint nm2simt2z `M` and `O` freeze as this neighbor-read composition.
- It does not reprint nm2cycfrmsl cyclic-frame transport reverse fail face hold as this neighbor-read.
- It does not select a unique outgoing or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require outgoing sides to be singletons.
- It does not sum either set.
- It does not replace transport by leftover-empty fail.
- It does not replace transport by leftover of `M` alone.
- It does not replace transport by leftover of `O` alone.
- It does not replace transport by existential opposite of signed locks.
- It does not replace transport by presence of an opposite pair in `O`.
- It does not replace transport by lexicographic unsigned `o1,o2` orientation.
- It does not replace transport by lex-one signed axis-order letters.
- It does not replace transport by unique signed `|O_i|=1` letters.
- It does not replace transport by opposite-pair leftover-axis orientation.
- It does not replace transport by unsigned axis units of `Axis(O)`.
- It does not replace transport by axis-cover without the frame.
- It does not replace transport by 1-in 2-out split without the frame.
- It does not replace transport by nm2oricyccz Orient reverse/face.
- It does not replace transport by nm2oricyclslz lex-largest cyclic Orient.
- It does not treat split fail as `UNDEFINED`.
- It does not treat empty cyclic `O_next` or `O_prev` as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace transport by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmcover axis-cover reverse hold face hold as this
  transport display.
- It does not reprint nm2oricyccz cyclic reverse hold face hold with
  `Orient(A)=+1` as this transport display.
- It does not reprint nm2oricyclslz lex-largest reverse fail face hold with
  `Orient(A)` fail and `Orient(B)=−1` as this transport display.
- It does not reprint nm2orionez lex-one reverse fail face hold with
  `Orient(A)` fail and `Orient(B)=+1` as this transport display.
- It does not reprint nm2slz axis-cover reverse fail face hold as this
  transport display.
- It does not reprint nm2axz axis-cover reverse hold face hold as this
  transport display.
- It does not reprint nm2ax12z 1-in 2-out split reverse hold face hold as
  this transport display.
- It does not reprint nm2chiralz lexicographic unsigned `o1,o2` reverse fail
  face hold with `+1,+1` as this transport display.
- It does not reprint nm2oridetz unique signed reverse fail face fail as
  this transport display.
- It does not reprint nm2orichz opposite-pair leftover-axis reverse fail
  face fail as this transport display.
- It does not reprint the 1-axis same-lock two-site seed as this member.
- It does not score the y-probes or the x-probes as this letter.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this transport display.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint the two-tick lock-count clock composition.
- This is not the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
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
two-axis same-lock seed process, neighbor-read of cyclic lex-smallest frame transport of
`(m,o_next,o_prev)` of `M` and `O` at `t+1` versus `t+2`, reverse/face at
each cut, and composition are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ1=t+1` and `τ2=t+2` | Theorem 1; frozen equal to `M` at `t` and equal across the two cuts |
| `O` at `τ1` and `τ2` | Theorem 1; outgoing dual includes partner `+e_2` at `A`; equal across the two cuts |
| split at `τ1` and `τ2` | Theorem 1; fail at `A`; HOLD at `B`,`C`,`D` at both cuts |
| unique signed `m`, index `i`, and cyclic `(o_next,o_prev)` | Theorem 1; singleton `M`; cyclic pair defined at each probe, Orient fail at `A` |
| integer `det(m,o_next,o_prev)` | Theorem 1; fail, `1`, `-1`, `-1` at both cuts |
| Orient at `τ1` and `τ2` | Theorem 1; fail, `+1`, `−1`, `−1` at both cuts |
| transport at `τ1` and `τ2` | Theorem 1; fail, hold, hold, hold at both cuts; nm2cycfrmsl leftover |
| neighbor-read of transport at `τ1` and `τ2` | Theorem 1; fail, hold, hold, hold at both cuts |
| scalar neighbor-read of Orient | Theorem 1; fail, hold, fail, hold at both cuts; not this letter |
| reverse from neighbor-read of cyclic lex-smallest frame transport at `τ1` and `τ2` | Theorem 2; `fail` at both cuts |
| face from neighbor-read of cyclic lex-smallest frame transport at `τ1` and `τ2` | Theorem 2; `hold` at both cuts |
| composition of neighbor-read at `τ1` versus `τ2` | Theorem 3; `hold` |
| unique outgoing lock | not required |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this transport display |
| leftover of exist-opposite HOLD | not this transport display |
| leftover of nmcover axis-cover HOLD | not this transport display |
| leftover of nm2axz axis-cover HOLD | not this transport display |
| leftover of nm2ax12z 1-in 2-out split HOLD | not this transport display |
| leftover of nm2chiralz lexicographic unsigned `o1,o2` | not this transport display |
| leftover of nm2orionez lex-one signed axis order | not this transport display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this transport display |
| leftover of nm2orichz opposite-pair leftover-axis | not this transport display |
| leftover of opposite-pair presence in `O` | not this transport display |
| leftover of nm2oricyccz Orient reverse/face | not this neighbor-read |
| leftover of nm2oricyclslz lex-largest cyclic | not this neighbor-read |
| leftover of nm2cycfrmsl cyclic-frame transport sending | not this neighbor-read |
| leftover of nm2cycfrmz cyclic-frame transport sending | not this neighbor-read |
| leftover of equal transport bits including fail=fail | not this neighbor-read |
| leftover of scalar neighbor-read of Orient | not this neighbor-read |
| leftover of unique nonnegative permutation sending | not this neighbor-read |
| y-probe or x-probe Orient on this seed | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nm2frmrdslz neighbor-read at `t+1` alone | not this composition |
| leftover of nm2frmrdslt2 cyclic-frame neighbor-read freeze | not this letter |
| leftover of nm2sfzfrmrdt2 three-axis far-face neighbor-read freeze | not this seed |
| leftover of nm2sfzfrmrd neighbor-read at `t+1` alone | not this composition |
| leftover of nm2sfzfrmt2 transport freeze without neighbor-read | not this neighbor-read |
| leftover of nm2sfzfrm cyclic lex-smallest frame transport | not this neighbor-read |
| leftover of nm2simt2z `M` and `O` freeze | not this neighbor-read equality |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| leftover of nm2oricyclz cyclic opposite z | not this display |
| leftover of nm2slz axis-cover | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the 1-axis same-lock two-site seed | not this display |
| leftover of the two-axis opposite seed | not this display |
| split fail scored as `UNDEFINED` | refused; transport fail |
| empty cyclic side scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| cyclic-frame transport as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of cyclic lex-smallest frame transport of `(m,o_next,o_prev)` of `M` and `O` at `t+1` versus `t+2` on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition. |
| V2 | Current main has no landed neighbor-read of cyclic lex-smallest frame-transport freeze t+1 versus t+2 reverse/face composition of timed `M` and `O` on these four z-probes of the two-axis same-lock seed. |
| V3 | Neighbor-read reports at two cuts, the reverse/face bits at each cut, and composition are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the transport HOLD bit at a formed six-neighbor at each of `t+1` and `t+2`, reverse fails from neighbor-read fail at `A` while face HOLDs at both cuts, composition HOLDs while composition at `t` versus `t+1` fails, scalar neighbor-read face fails because scalar fails at `C`, unique nonnegative sending HOLDs at `D` and fails at `A`,`B`,`C` so unique-nonnegative face fails, equal transport bits including fail=fail HOLDs at a transport-fail site where this neighbor-read fails, nm2frmrdslz scores only one cut, nm2frmrdslt2 inspects left-action cyclic-frame sending, nm2sfzfrmrdt2 is the three-axis far-face opposite seed, and nm2cycfrmsl sending inspects `T` which this neighbor-read does not. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace transport by leftover-empty fail,
does not replace transport by leftover of `M` alone or leftover of `O`
alone, does not replace transport by existential opposite of signed locks,
does not replace transport by presence of an opposite pair in `O`, does not
replace transport by nm2chiralz lexicographic unsigned `o1,o2`, does not
replace transport by nm2orionez lex-one signed axis order, does not replace
transport by nm2oridetz unique signed `|O_i|=1`, does not replace transport
by nm2orichz opposite-pair leftover-axis, does not replace transport by
nmcover axis-cover, does not replace transport by nm2axz axis-cover, does
not replace transport by nm2ax12z 1-in 2-out split, does not identify this
display with the 1-axis same-lock two-site seed, does not identify it with
nm2oricyccz cyclic next/prev on the opposite seed, does not identify it
with nm2oricyclslz lex-largest on this seed, does not identify it with
nm2slz axis-cover, and does not identify it with nmunopp union. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2frmrdslz neighbor-read at t+1 | reuse the t+1 reverse fail and face hold | nm2frmrdslz scores only `τ=t+1`; this letter first displays those bits at `t+2` and scores composition | ATTEMPTED |
| nm2frmrdslt2 cyclic-frame neighbor-read freeze | reuse same-lock reverse fail face hold composition hold | nm2frmrdslt2 inspects left-action cyclic-frame sending `T`; this letter is neighbor-read of nm2sfzfrm `F(r)=F(q)P` | ATTEMPTED |
| nm2sfzfrmrdt2 three-axis far-face freeze | reuse far-face reverse hold face hold composition hold | far-face third pair sits on `−z`; this seed is two disjoint same-lock pairs and reverse fails from split fail at `A` | ATTEMPTED |
| nm2sfzfrmrd neighbor-read at t+1 | reuse far-face t+1 neighbor-read | nm2sfzfrmrd is three-axis far-face at one cut; this letter is two-axis same-lock freeze | ATTEMPTED |
| nm2sfzfrmt2 transport freeze | reuse transport bits without neighbor-read | transport face HOLDs here, but neighbor-read is the scored object | ATTEMPTED |
| nm2sfzfrm cyclic lex-smallest frame transport | reuse transport reverse/face without neighbor-read | transport HOLDs at `B,C,D`; neighbor-read additionally requires a formed 6-NN with transport HOLD | ATTEMPTED |
| nm2simt2z M and O freeze | reuse equality of M and O across cuts | M and O freeze here, but composition is neighbor-read equality, not the sets | ATTEMPTED |
| nm2cycfrmsl cyclic-frame transport sending | reuse signed-permutation sending of `F(q)` to `F(r)` | sending inspects `T`; this neighbor-read reads only the transport HOLD bit at a formed 6-NN. On this member the four probe bits agree, but at `(0,-1,1)` equal-bit HOLDs while neighbor-read fails | ATTEMPTED |
| nm2cycfrmz cyclic-frame transport | reuse opposite-seed transport reverse hold and face hold | opposite-seed transport HOLDs at `A`; here transport at `A` fails from split fail, so neighbor-read at `A` fails and reverse fails | ATTEMPTED |
| equal transport bits including fail=fail | HOLD if some formed 6-NN has the same transport bit | at `(0,-1,1)` transport fails and a formed 6-NN also fails, so equal-bit HOLDs while neighbor-read fails, not UNDEFINED | ATTEMPTED |
| scalar neighbor-read of Orient | reuse equal Orient sign at some formed 6-NN | scalar fails at `A` and at `C`; scalar reverse fails and scalar face fails while this reverse fails from a different object and this face HOLDs | ATTEMPTED |
| unique nonnegative permutation sending | require a unique sending with no minus signs | unique nonnegative sending HOLDs at `D` and fails at `A`,`B`,`C`; unique-nonnegative face fails while this face HOLDs; uniqueness is not required | ATTEMPTED |
| nm2oricyccz cyclic opposite z | reuse opposite-seed reverse hold and face hold | nm2oricyccz has split HOLD at `A` and `Orient(A)=+1` equal to `Orient(B)`; here split fails at `A` from overlapping `e_2` and transport at `A` is fail, so reverse fails | ATTEMPTED |
| nm2oricyccz Orient on this seed | reuse Orient reverse fail and face hold | Orient signs are `fail,+1,−1,−1`; transport bits are `fail,hold,hold,hold`; reverse/face bits match while the object differs | ATTEMPTED |
| nm2oricyclslz lex-largest same-lock z | reuse lex-largest reverse fail and face hold | lex-largest signs are `fail,−1,+1,+1`; lex-smallest signs are `fail,+1,−1,−1`; lex-largest picks `−e` on mixed axes while lex-smallest picks `+e` | ATTEMPTED |
| nm2orionez lex-one same-lock z | reuse lex-one reverse fail and face hold | lex-one signs match cyclic lex-smallest on this member at `B,C,D`; cyclic `m=+e_2`, `O={+e_1,+e_3}` has Orient `+1` while lex-one has `−1` | ATTEMPTED |
| nm2slz axis-cover | reuse cover reverse fail and cover face hold | cover does not report signed frames or a sending matrix; cover HOLDs at `C` and at `D` while transport HOLDs there | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face hold | unsigned face HOLDs with `+1,+1` matching this face, but unsigned Orient at `C` is `+1` while cyclic Orient at `C` is `−1` | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed face fails while this face HOLDs; an opposite pair in `O` makes `|O_i|≠1` but lex-smallest still picks `+e` at `B`,`C`,`D` | ATTEMPTED |
| nm2orichz opposite-pair leftover-axis | reuse leftover-axis reverse and face | leftover-axis reverse fails and face fails (`fail,−1` and `−1,+1`); this face HOLDs | ATTEMPTED |
| nm2axz axis-cover | reuse opposite-seed cover reverse hold and cover face hold | nm2axz HOLDs at `A`; here cover fails at `A` because `O(A)` includes partner `+e_2` | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse opposite-seed split reverse hold and split face hold | opposite split HOLDs at `A`; here split fails at `A`; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails with these bits, leftover face fails while this face HOLDs; unique signed `O={+e_1,+e_3}` has empty leftover and Orient `+1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal; leftover of `M` face fails while this face HOLDs | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is empty, leftover reverse fails for a one-sided empty leftover, not transport fail from split fail | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `O` holds while transport reverse fails; exist-opposite face of signed `O` fails while this face HOLDs | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence HOLDs at each of `A,B,C,D`, so that reverse HOLDs while this reverse fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; transport is a signed-permutation relation of cyclic frames | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this transport is fail, not `UNDEFINED` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member both fail at `A` and agree at `B,C,D`; flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient from `+1` to `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is transport fail, not UNDEFINED; `A` fails from overlapping cover, not from 2-in 1-out | ATTEMPTED |
| empty cyclic side as `UNDEFINED` | treat empty `O_next` or `O_prev` as unformed | empty cyclic side is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis same-lock two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, Orient fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=0` and split HOLDs at `C` | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe reverse fails (`−1,+1`) and y-face fails; this letter is the four z-probes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the four z-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores neighbor-read of cyclic lex-smallest frame transport of own incoming and outgoing at `t+1` versus `t+2` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face hold on the two-axis same-lock seed | ATTEMPTED |
| 1-axis same-lock two-site reuse | reuse `+e_1/+e_1` alone | different seed; this member is two disjoint same-lock pairs | ATTEMPTED |
| sum of a set | replace transport by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `+e_2+e_3` while transport at `A` fails | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the transported frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of transport with leftover of
`M` alone, missing identification of transport with leftover-empty fail, missing
identification of transport with existential opposite of signed locks, missing
identification of transport with presence of an opposite pair in `O`, missing
identification of transport with nm2chiralz lexicographic unsigned `o1,o2`,
missing identification of transport with nm2orionez lex-one, missing
identification of transport with nm2oridetz unique signed `|O_i|=1`, missing
identification of transport with nm2orichz opposite-pair leftover-axis, missing
identification of transport with nmcover axis-cover, missing identification of
transport with nm2axz axis-cover, missing identification of transport with
nm2ax12z 1-in 2-out split, missing identification of transport with nm2oricyccz
cyclic next/prev, missing identification of transport with nm2oricyclslz
lex-largest, missing identification of transport with nm2slz axis-cover,
missing identification of this seed with the 1-axis same-lock two-site seed,
and missing Record identification of transport reverse are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock seed pairs `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ1=t+1`
and `τ2=t+2`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
next/prev axes of `Axis(M)`, lex-smallest signed outgoing letter per cyclic
axis under `+e < −e`, integer determinant sign, integer sending matrix of
frame columns, signed-permutation transport to a formed six-neighbor, empty
cyclic side as Orient fail not `UNDEFINED`, split fail as transport fail
not `UNDEFINED`, four z-probes with seed `A`, second pair as a new seed not
a formed child, and mixed remains a set are declared. No uniqueness of
outgoing locks, no six-neighbor lock union as the scored object, no
lock-count clock, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
transport `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | neighbor-read of the cyclic lex-smallest frame transport HOLD bit at a formed 6-NN | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports at t+1 and t+2, reverse/face at each cut, composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for transport reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out frames. None
is taken here.

### N7 — hostile steelman

**Steelman:** Neighbor-read reverse fail and face hold are only leftover of
nm2cycfrmsl cyclic-frame transport sending, or of equal transport bits
including fail=fail, or of neighbor-read of the scalar Orient sign, or of
nm2oricyccz cyclic next/prev on opposite z; they are only leftover of
nm2oricyccz Orient reverse/face on this seed; they are only leftover of
nm2oricyclslz lex-largest; they are only leftover of nm2orionez lex-one on
this seed; they are only leftover of nm2slz cover; nm2chiralz unsigned
`o1,o2` already answers mixed `O`; unique signed `|O_i|=1` already answers
mixed `O`; cover reverse and split reverse already answer the three-axis
occupation; leftover of `M` alone already answers reverse; leftover of `O`
alone already answers reverse; exist-opposite of signed `O` already
answers reverse; opposite-pair leftover-axis already answers handedness;
mixed #7188 already reported fail/fail; the second pair is only the formed
child `(0,0,1)` of the 1-axis seed; unique outgoing letters should be
required; and unsigned incoming axis already gives the same signs because
each `M` letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Neighbor-read reverse fails because neighbor-read at `A` is
fail and neighbor-read at `B` is hold. Neighbor-read face HOLDs because
both bits HOLD. Scalar neighbor-read of Orient fails at `A` and at `C`, so
scalar reverse fails and scalar face fails while this face HOLDs. Unique
nonnegative permutation sending HOLDs at `D` and fails at `A`, `B`, and
`C`, so unique-nonnegative face fails while this face HOLDs. Equal transport bits
including fail=fail HOLDs at `(0,-1,1)` while neighbor-read fails there.
Cover and split fail reverse and HOLD face on this member and do not score
that signed-permutation relation at `C` and at `D`. nm2oricyccz on the
opposite seed has `Orient(A)=+1` with split HOLD and reverse HOLDs; here
`O(A)` includes partner `+e_2`, split fails, transport at `A` is fail, and
reverse fails. nm2oricyccz Orient on this same-lock seed has signs
`fail,+1,−1,−1`; this display has transport `fail,hold,hold,hold`.
nm2oricyclslz lex-largest on this same-lock seed has Orient
`fail,−1,+1,+1`; this Orient is `fail,+1,−1,−1`. nm2orionez lex-one on this
same-lock seed has Orient `fail,+1,−1,−1` matching this Orient on this
member, while cyclic `m=+e_2`, `O={+e_1,+e_3}` disagrees. nm2slz cover
reverse fails from overlapping `e_2` but does not report transport HOLD at
`C` and at `D`. Lexicographic unsigned `o1,o2` reverse fails with
`fail,+1` and face HOLDs with `+1,+1`; unsigned Orient at `C` is `+1` while
cyclic Orient at `C` is `−1`. Unique signed `|O_i|=1` reverse fails and
face fails because mixed opposite pairs occupy `O`; this face HOLDs.
Opposite-pair leftover-axis reverse fails and face fails; this face HOLDs.
Presence of an opposite pair in `O` HOLDs at each of the four z-probes, so
pair-presence reverse HOLDs, while this reverse fails. Leftover of `M`
alone at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`: nonempty unequal.
Leftover of `O` alone at `A` is empty. Exist-opposite reverse of signed `O`
holds while transport reverse fails. Unique outgoing letters would assign
`UNDEFINED` at mixed `O(A)`; this transport is fail, not `UNDEFINED`. On
unique signed `O={+e_1,+e_3}` leftover is empty while Orient is `+1`, so
leftover-empty fail is not this predicate. Mixed #7188 is a different
z-symmetric process with mixed `M`. The second pair is a new seed, not a
formed child: `(0,0,1)` is recorded at tick 0 with lock `+e_2`, whereas the
1-axis child forms at tick 1 with lock `+e_3`. Reverse cyclic lex-smallest frame
transport is HOLD iff transport HOLDs at `A` and at `B`, not leftover of
nm2oricyccz cyclic next/prev and not leftover of nm2slz axis-cover.

### N8 — cross-cycle echo

nm2slz axis-cover on this two-axis same-lock seed reported cover fail at
`A` from overlapping `e_2`, cover HOLD at `B`,`C`,`D`, reverse fail, and
face hold. nm2oricyccz cyclic next/prev on the two-axis opposite seed
reported `Orient(A)=+1` with split HOLD, reverse hold, and face hold.
nm2oricyclslz lex-largest on this same-lock seed reported Orient
`fail,−1,+1,+1`, reverse fail, and face hold. nm2orionez lex-one on this
same-lock seed reported Orient `fail,+1,−1,−1`, reverse fail, and face
hold. nm2axz cover on the opposite seed reported cover HOLD at each of the
four z-probes, reverse hold, and face hold. nm2ax12z 1-in 2-out split on
the opposite seed reported split HOLD at each of the four z-probes,
reverse hold, and face hold. Leftover axis reported empty leftover at each
of four z-probes, leftover reverse fail, and leftover face fail. The four
y-probes of this same seed reported cyclic Orient `−1` at `A` from
`{+e_2,−e_3}` and Orient fail at `D` from split fail, so y-reverse fails
and y-face fails. This note is not those displays: it reports neighbor-read of cyclic lex-smallest frame
transport of `(m,o_next,o_prev)` of `M` and `O` at `τ1=t+1` versus
`τ2=t+2` on the two-axis same-lock seed, with `t(A)=0`, `t(B)=1`,
`t(C)=1`, and `t(D)=1`, `transport` fail,hold,hold,hold at both cuts,
`neighbor-read` fail,hold,hold,hold at both cuts, reverse fail at both
cuts, face hold at both cuts, and composition hold, while scalar
neighbor-read fails at `A` and at `C` at both cuts. Cover and split do
not score handedness. This is not leftover of nm2frmrdslz at `t+1` alone. This is not leftover of nm2frmrdslt2. This is not leftover of nm2sfzfrmrdt2. This is not leftover of nm2sfzfrmrd. This is not leftover of nm2sfzfrmt2.

**Gate disposition:** PASS for the neighbor-read of cyclic lex-smallest frame-transport
`t+1` versus `t+2` reverse/face composition reports above. FAIL / DO NOT SHIP for “the predicate
equals the named sign,” “the predicate equals the unique singleton lock
vector,” “the predicate equals six-neighbor lock union,” “the predicate
equals leftover-empty fail,” “the predicate equals leftover of `M`
alone,” “the predicate equals leftover of `O` alone,” “the predicate
equals exist-opposite HOLD,” “the predicate equals opposite-pair presence
in `O`,” “the predicate equals nm2oricyccz cyclic HOLD,” “the predicate
equals nm2oricyclslz lex-largest HOLD,” “the predicate equals nm2orionez
lex-one HOLD,” “the predicate equals nm2slz axis-cover HOLD,” “the
predicate equals nm2chiralz lexicographic unsigned `o1,o2` HOLD,” “the
predicate equals nm2oridetz unique signed HOLD,” “the predicate equals
nm2orichz opposite-pair leftover-axis HOLD,” “the predicate equals nm2frmrdslt2 cyclic-frame neighbor-read freeze HOLD,” “the predicate equals nm2sfzfrmrdt2 three-axis far-face neighbor-read freeze HOLD,” “the predicate equals nm2sfzfrmrd t+1 HOLD,” “the predicate equals nm2sfzfrmt2 transport freeze HOLD,” “the predicate equals nm2sfzfrm transport HOLD,” “the predicate equals
nm2cycfrmsl cyclic-frame transport sending HOLD,” “the predicate equals
nm2cycfrmz cyclic-frame transport sending HOLD,” “the predicate equals
equal transport bits including fail=fail HOLD,” “the predicate equals
scalar neighbor-read of Orient HOLD,” “the predicate equals unique
nonnegative permutation sending HOLD,” “the predicate equals nmcover
axis-cover HOLD,” “the predicate equals nm2axz axis-cover HOLD,” “the
predicate equals nm2ax12z 1-in 2-out split HOLD,” “the predicate equals
the 1-axis same-lock two-site seed,” “the predicate equals nmunopp
union,” “bits are Admissibility,” “split fail is UNDEFINED,” “empty cyclic
side is UNDEFINED,” or “reverse neighbor-read of cyclic lex-smallest frame transport
holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`
and `t+2`, reports split of the pair, reports the unique signed incoming
letter, the axis index `i`, and the cyclic next/prev lex-smallest outgoing
letters, reports the integer determinant and its sign, reports the cyclic
frame `F` and signed-permutation transport to a formed six-neighbor,
reports neighbor-read of that transport HOLD bit at a formed
six-neighbor at each cut, lists new records in `B_3(0)` between `t` and
`t+1` and between `t+1` and `t+2` that meet a probe's six-neighbors, and
checks Theorems 1--3. It also checks that Orient is
fail,`+1`,`−1`,`−1` from cyclic lex-smallest columns, that transport is
fail,hold,hold,hold, that neighbor-read is fail,hold,hold,hold, that
reverse fails and face HOLDs from neighbor-read while scalar reverse fails
and scalar face fails, that unique nonnegative permutation sending HOLDs at `D` and fails at `A`, `B`, and `C` so unique-nonnegative face fails,
that split fail is transport fail not `UNDEFINED` and
transport fail is neighbor-read fail not `UNDEFINED`, that empty cyclic
side is Orient fail not `UNDEFINED`, that equal transport bits including
fail=fail HOLDs at `(0,-1,1)` while neighbor-read fails there, that
nm2oricyccz opposite-seed Orient at `A` is `+1` while this Orient at `A`
is fail and that opposite reverse HOLDs while this reverse fails, that the
1-axis same-lock two-site seed is a different member with Orient fail at
`C`, that leftover-empty fail is a different predicate, that leftover of
`M` alone and leftover of `O` alone are different objects, that mixed sets
remain sets, that unique-letter Orient is `UNDEFINED` at mixed `O`, that
lexicographic unsigned Orient at `C` is `+1` while this Orient at `C` is
`−1`, that lex-largest Orient at `B` is `−1` while this Orient at `B` is
`+1`, that unique signed face fails while this face HOLDs, that
opposite-pair leftover-axis reverse fails while this reverse also fails
from a different object, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
that the second pair is a new seed not a formed child, that neither pair
is opposite, that the y-probes and x-probes of this seed are not this
letter, and that the display is not the two-tick lock-count clock
composition. No runner cache is written.
