---
claim_id: three_axis_farface_opposite_xprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of the cyclic lex-smallest frame transport at t+1 on the four x-probes of the three-axis far-face opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_farface_opposite_xprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Cyclic Lex-Smallest Frame Transport At t+1 Reverse And Face On Four X-Probes Of The Three-Axis Far-Face Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of cyclic lex-smallest frame transport of `F=(m,o_next,o_prev)` of the 1-in 2-out
frame of simultaneous earliest incoming set `M` and outgoing dual `O` at
each probe's `τ=t+1`, and reverse/face from that neighbor-read, on the four
x-probes of the three-axis far-face opposite seed in `B_3(0)={n:n·n<=9}`. Same
process and x-probes as nm2axx. `M` and `O` as nm2ax12x. Orient as
nm2oricyccz. Transport as nm2sfzfrm. Let `t(q)` be the
formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of
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
likewise. `Orient(q)` is the sign of the integer determinant of the 3×3
matrix with columns `m`, `o_next`, `o_prev`. If split fails, Orient fails,
not `UNDEFINED`. When split HOLDs, `F(q)=(m,o_next,o_prev)`. Transport
HOLDs at `q` if and only if split HOLDs at `q`, `Orient(q)` is `±1`, and
some formed 6-NN `r` has split HOLD, `Orient(r)` `±1`, and the 3×3 integer
matrix sending the columns of `F(q)` to the columns of `F(r)` is a signed
permutation with determinant `Orient(q)*Orient(r)`. If split or Orient
fails at `q`, transport fails, not `UNDEFINED`. Neighbor-read HOLDs at
`q` if and only if transport HOLDs at `q` and some formed 6-NN `r` has
transport HOLD. If transport fails at `q`, neighbor-read fails, not
`UNDEFINED`. Reverse HOLDs if and only if neighbor-read HOLDs at `A` and
at `B`. Face HOLDs if and only if neighbor-read HOLDs at `C` and at `D`.
Cover and split do not score handedness. Equal `±1` Orient signs do not
score a 6-NN signed permutation of `F`. This is not leftover of nm2sfzfrm
cyclic lex-smallest frame transport reverse HOLD whose sending inspects a
signed permutation without a second-neighbor transport HOLD. This is not
leftover of scalar neighbor-read of Orient. This is not leftover of equal
transport bits including fail=fail. This is not leftover of nm2frmrdz
neighbor-read of lex-largest frame transport on the two-axis opposite seed.
This is not leftover of nm2oricycl3fz Orient reverse HOLD face HOLD from equal
signs. This is not leftover of nm2orichz leftover-axis reverse HOLD whose
face fails because C and D swap `(m,pair)` columns. This is not leftover
of nm2orionez lex-one reverse fail whose face HOLDs from `e1<e2<e3` order
independent of `m`. This is not leftover of nm2chiralz lexicographic
unsigned `o1,o2` orientation. This is not leftover of nm2oridetz unique
signed outgoing letters. This is not leftover of nm2axx axis-cover. This
is not leftover of nm2ax12x 1-in 2-out split. This is not leftover of
nm2oricyclz two-axis HOLD. This is not leftover of cyclic lex-largest. This is not leftover of leftover-of-`M` alone.
This is not leftover of leftover-of-`O` alone. This is not leftover-empty
fail of leftover axis. This is not leftover of nmunopp union. This is not
leftover of nmt2opp `M` frozen at `t`. This is not leftover of nmot2opp
two-tick composition. This is not leftover of nmoutopp untimed
eventual-`O`. This is not leftover of mixed #7188 fail/fail. This is not
leftover of the 1-axis opposite two-site seed. This is not leftover of the
same-lock two-site seed. This is not leftover of the two-axis opposite
seed of nm2oricyclz. The second pair is a new seed, not a formed child.
The third pair is a new seed, not a formed child. Uniqueness is not
required. Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_farface_opposite_xprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_farface_opposite_xprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_reverse_face_2026_08_15.py)

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
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev
lex-smallest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m` and the
lex-smallest signed outgoing letter on the cyclic next and prev axes of
`Axis(M)` under `+e < −e`. When split HOLDs, `F=(m,o_next,o_prev)`.
Transport of that frame at a probe HOLDs if some formed six-neighbor has
split HOLD and Orient `±1` and the integer matrix sending the columns of
`F(q)` to the columns of `F(r)` is a signed permutation with determinant
`Orient(q)*Orient(r)`. Neighbor-read of that transport HOLDs if transport
HOLDs at the probe and some formed six-neighbor also has transport HOLD.
Reverse and face are scored on neighbor-read HOLD at the paired probes. Named signs `{+,−}` of locks are a coarser
readout and are not used as the object. A singleton unique outgoing lock
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
is not used. Leftover-empty fail of unsigned leftover axis sets is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of cyclic lex-smallest frame transport of (m,o_next,o_prev) of the 1-in 2-out frame of M and O at t+1 on the four x-probes of the three-axis far-face opposite seed, Orient fail/hold/hold/fail, transport fail/hold/hold/fail, neighbor-read fail/hold/hold/fail, reverse fail and face fail from neighbor-read; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_farface_opposite_xprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_reverse_face
target_blocker_text: "display neighbor-read of cyclic lex-smallest frame transport reverse/face on the four x-probes of the three-axis far-face opposite seed, not transport without neighbor-read, not scalar neighbor-read of Orient, not equal transport bits including fail=fail, not equal Orient signs, not leftover-axis, not lex-one e1<e2<e3, not unique |O_i|=1, not unsigned axis units, not cover, not split, not two-axis HOLD"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of cyclic lex-smallest frame transport of (m,o_next,o_prev) of M and O at t+1 displayed; do not write the bits into Admissibility, do not reduce to nm2sfzfrm transport without neighbor-read, do not reduce to scalar neighbor-read of Orient, do not reduce to equal transport bits including fail=fail, do not reduce to equal Orient signs, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-largest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace neighbor-read by unique outgoing letters, do not replace neighbor-read by existential opposite of signed locks, do not replace neighbor-read by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of cyclic lex-smallest frame transport of (m,o_next,o_prev) of M and O at t+1 on the four x-probes of the three-axis far-face opposite seed and reverse/face from that neighbor-read; reverse fail and face fail; displayed, not adopted"
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
neighbor-read of cyclic lex-smallest frame transport of `F=(m,o_next,o_prev)` of `M` and
`O` is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is not a seed. `C` is `(2,0,0)`, not the far-face third-pair
seed. Same process as the far-face seed of nm2sfzfrmrd; x-probes as nm2ax.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. Site `(0,0,−1)` locks `+e_3`. Site `(0,1,−1)`
locks `−e_3`. The second pair is a new seed, not a formed child of the
first pair. The third pair is a new seed, not a formed child, and sits on
the `−z` face opposite the x-probes: on the two-axis opposite seed those
sites form at tick 1 locking `−e_3`. This seed is not the two-axis
opposite seed of nm2oricyclz. This seed is not
the 1-axis opposite two-site seed `{0,(0,1,0)}` with only `+e_1/−e_1`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
same-lock two-site seed `+e_1/+e_1`. This seed is not the z-symmetric
three-site seed `{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric
three-site seed that also records `(0,-1,0)` at tick 0.

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

Oriented frame at the same cut:

```text
When split HOLDs, m is the unique signed letter in M.
i in {1,2,3} is the axis index of m.
e_next = e_{i+1} with 3+1→1. e_prev = e_{i-1} with 1−1→3.
O_next = O ∩ {±e_next}. O_prev = O ∩ {±e_prev}.
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e. o_next is lex-smallest in O_next (hence +e if both signs).
o_prev likewise.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
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

When split HOLDs, the cyclic frame is the ordered triple

```text
F(q) = (m, o_next, o_prev).
```

Transport of that frame at the same cut:

```text
transport(q) HOLDs iff split HOLDs at q, Orient(q) is ±1,
and some formed 6-NN r has split HOLD, Orient(r) ±1,
and the 3×3 integer matrix S sending the columns of F(q)
to the columns of F(r) (F(r) = F(q) S) is a signed permutation
with det(S) = Orient(q)*Orient(r).
If split or Orient fails at q, transport fails, not UNDEFINED.
If q is unformed at τ, transport is UNDEFINED.

Neighbor-read HOLDs at q iff transport(q) HOLDs
and some formed 6-NN r has transport(r) HOLD.
If transport fails at q, neighbor-read fails, not UNDEFINED.
UNDEFINED if transport is UNDEFINED.
Uniqueness of r is not required.
```

Uniqueness of the transporting neighbor is not required. Mixed remains a
set. Occupancy of sites is not used. A six-neighbor star is not the letter.

Neighbor-read of the scalar Orient sign HOLDs at `q` if and only if
`Orient(q)` is `±1` and some formed six-neighbor has the same sign. That
is a different object: it HOLDs at `A`, `B`, and `D` and fails at `C` on
this member while neighbor-read of transport HOLDs at each of `A,B,C,D`.
Equal transport bits including fail=fail is a different object: at
`(0,-1,1)` transport fails and a formed six-neighbor also fails, so
equal-bit HOLDs while neighbor-read fails.

Reverse neighbor-read of cyclic lex-smallest frame transport holds if and only if neighbor-read HOLDs at `A`
and at `B`. Face neighbor-read of cyclic lex-smallest frame transport holds if and only if neighbor-read
HOLDs at `C` and at `D`. Either side `UNDEFINED` is `UNDEFINED`. Else if
both sides HOLD, reverse or face HOLDs. Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse and face without reading
cyclic signed columns or a 6-NN signed permutation of `F`. Identifying
split reverse with this reverse is refused: split HOLDs reverse and face
without the cyclic order of `Axis(M)` and without transport of `F`.
Identifying nm2oricycl3fz Orient reverse with this reverse is refused:
Orient reverse HOLDs from equal `±1` signs at `A` and at `B` without a
6-NN signed permutation of `F`; leftover-axis face fails with `+1,−1` while this face HOLDs, and unique signed fails at each probe while transport HOLDs. Identifying leftover-empty fail with this reverse is refused:
leftover-empty fail scores empty leftover as reverse fail and face fail,
while this reverse HOLDs and this face HOLDs; leftover of the union is
empty while Orient is a sign (`+1,+1,−1,−1`); on unique signed
`O={+e_1,+e_3}` leftover is empty while Orient is `+1`. Identifying
lexicographic unsigned `o1,o2` with this reverse is refused: unsigned
reverse fails with `−1,+1` while this reverse HOLDs with `+1,+1`; unsigned
face HOLDs with `+1,+1` while this face HOLDs with `−1,−1`, and unsigned `o1,o2` at `B`
is `(e_2,e_3)` as cyclic is `(+e_2,+e_3)`. Identifying nm2orionez
lex-one signed `e1<e2<e3` with this reverse is refused: lex-one reverse
fails from axis order independent of `m` while this reverse HOLDs, and
lex-one face HOLDs with `−1,−1` as this face HOLDs.
Identifying unique signed `|O_i|=1` with this reverse is refused: unique
signed Orient fails at each of `A,B,C,D` from mixed opposite pairs, while
this Orient is `+1,+1,−1,−1`. Identifying leftover-axis orientation with
this reverse is refused: leftover-axis reverse HOLDs with `−1,−1` as this
reverse HOLDs, but leftover-axis face fails with `+1,−1` while this face
HOLDs with `−1,−1`. Identifying cyclic lex-largest with this reverse is
refused: lex-largest reverse HOLDs with `−1,−1` and face HOLDs with
`+1,+1`, while this Orient is `+1,+1,−1,−1`. Identifying nm2oricyclz
two-axis HOLD with this reverse is refused: two-axis reverse HOLDs and
face HOLDs with `−1,−1,+1,+1` signs on these x-probes, but that
seed has four tick-0 sites and forms `(0,0,−1)` at tick 1 locking `−e_3`,
while this third pair is a new seed at tick 0 locking `+e_3/−e_3`.
Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, Orient, transport, and neighbor-read at `τ=t+1`

On this process the four x-probes form. Compare to leftover axis: leftover
at `A` and at `D` is `{e_2}`, leftover at `B` and at `C` is empty, leftover
reverse fails and leftover face fails, as this reverse fails and this face
fails, but leftover of the union is not the neighbor-read bit: neighbor-read
HOLDs at `B` while leftover at `B` is empty. Compare to nm2axx cover and
nm2ax12x split: cover and split fail reverse and fail face on this member
without cyclic signed columns. Compare to nm2oricyclz on the two-axis
opposite seed: that seed has four tick-0 sites. Compare to nm2oridetz unique
signed outgoing letters: unique signed fails at `B` and at `C` while
neighbor-read HOLDs there. Compare to cyclic lex-largest: at `B` lex-largest
Orient is `−1` while this Orient is `+1`; at `C` lex-largest is `+1` while
this Orient is `−1`. This display reads the neighbor-read of cyclic
next/prev lex-smallest frame transport of those same timed sets:

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
m(A) = fail
i(A) = fail
o_next(A) fail
o_prev(A) fail
det(A) = fail
Orient(A) = fail
m(B) = +e_1
i(B) = 1
o_next(B) = +e_2
o_prev(B) = +e_3
det(B) = 1
Orient(B) = +1
m(C) = +e_1
i(C) = 1
o_next(C) = −e_2
o_prev(C) = +e_3
det(C) = -1
Orient(C) = −1
m(D) = fail
i(D) = fail
o_next(D) fail
o_prev(D) fail
det(D) = fail
Orient(D) = fail
F(A) = fail
F(B) = (+e_1, +e_2, +e_3)
F(C) = (+e_1, −e_2, +e_3)
F(D) = fail
transport(A) = fail
transport(B) = hold
transport(C) = hold
transport(D) = fail
neighbor-read(A) = fail
neighbor-read(B) = hold
neighbor-read(C) = hold
neighbor-read(D) = fail
scalar neighbor-read(A) = fail
scalar neighbor-read(B) = hold
scalar neighbor-read(C) = fail
scalar neighbor-read(D) = fail
witness(A) = fail
witness(B) = (0, 1, 1)
witness(C) = (2, 1, 0)
witness(D) = fail
read-witness(A) = fail
read-witness(B) = (0, 1, 1)
read-witness(C) = (2, 1, 0)
read-witness(D) = fail
```

`A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with mixed
incoming `{+e_3, −e_3}`. Mixed remains a set: `M(A,τ)` and `M(D,τ)` each
have two incoming steps on one axis, `O(B,τ)` has three outgoing steps,
`O(C,τ)` has three outgoing steps, and `O(D,τ)` has two outgoing steps on
one axis. Unique incoming letters would assign `UNDEFINED` at mixed `M(A)`
and mixed `M(D)`. Unique outgoing letters would assign `UNDEFINED` at
mixed `O(B)`, `O(C)`, and `O(D)`. Unique signed `|O_i|=1` fails at `B` and
at `C` because those outgoing sets have an opposite pair, while
neighbor-read HOLDs there. Split fails at `A` and at `D` because
`Axis(M)∪Axis(O)={e_1,e_3}` misses `e_2`, so Orient fails, transport
fails, and neighbor-read fails. Cover and split HOLD at `B` and at `C` and
do not score that cyclic lex-smallest Orient is `+1` at `B` and `−1` at
`C`. Transport HOLDs at `B` and at `C`. Neighbor-read HOLDs at `B` and at
`C`. The first formed 6-NN in six-step order that transports `F` is seed
`(0,1,1)` at `B` and `(2,1,0)` at `C`. The first formed 6-NN in six-step
order with transport HOLD is the same two sites. Uniqueness of that
witness is not required. Scalar neighbor-read of Orient HOLDs at `B` and
fails at `A`, at `C`, and at `D`. Equal transport bits including fail=fail
HOLDs at `(0,-1,1)` while neighbor-read there fails. At `B`, `i=1` so
`e_next=e_2` and `e_prev=e_3`; mixed `O_prev={±e_3}` yields `o_prev=+e_3`.
At `C`, `i=1` so `e_next=e_2` and `e_prev=e_3`; mixed `O_prev={±e_3}`
yields `o_prev=+e_3` and `o_next=−e_2`. Cyclic lex-largest at `B` picks
`o_prev=−e_3` and reports `−1`, while this Orient at `B` is `+1`. Leftover-axis
at `B` is pair `+e_3` leftover `+e_2` and that Orient is `−1`. O is not M.

On the 1-axis opposite two-site seed, `A=(1,0,0)` forms at tick 3 with
mixed `M={+e_2,+e_3,−e_3}` and cover HOLDs as 2-in 1-out, so split fails at
`A`. That is leftover of the first pair. Here the second pair and the third
pair are new seeds, not formed children, and the third pair sits on the
`−z` face. On the y-probes of this same seed, split HOLDs at `A` with
`m=−e_1` so `i=1`, `o_next=+e_2`, `o_prev=−e_3`, and cyclic Orient at
that y-probe is `+1`. Y-probe `B` is `+1`, so y-probe reverse HOLDs while
this x-probe reverse fails. Y-probe `D` has split fail, so y-face fails as
this face fails. On the z-probes of this same seed, neighbor-read reverse
HOLDs and face HOLDs.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(2,0,0)` forms
at tick 3, so it is a new 6-NN of `A`. Site `(2,1,0)` forms at tick 3, so
it is a new 6-NN of `D`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at `A`, at `B`, and
at `C`, while `O(D,t)={−e_1}`; split fails at each probe, and Orient is
fail, not UNDEFINED.

## Theorem 2 — reverse from neighbor-read of cyclic lex-smallest frame transport at `τ`

Reverse neighbor-read of cyclic lex-smallest frame transport holds if and only if neighbor-read HOLDs at `A`
and at `B`. `neighbor-read(A)=fail` and `neighbor-read(B)=hold`. Reverse fails.
This is HOLD iff both sides neighbor-read, not leftover of nm2sfzfrm
transport without a second-neighbor transport HOLD, not leftover of
scalar neighbor-read of Orient, not leftover of equal transport bits
including fail=fail, not leftover of equal `±1` Orient signs, not leftover of nm2chiralz lexicographic unsigned `o1,o2`, not
leftover of nm2oridetz unique signed outgoing letters, not leftover of
nm2orichz leftover-axis, not leftover of nm2orionez lex-one, not leftover
of nm2axx axis-cover, not leftover of nm2ax12x 1-in 2-out split, not
leftover of nm2oricyclz two-axis HOLD, not leftover-empty fail, and not
exist-opposite. On this member transport reverse also fails and Orient reverse also fails,
because `A` has split fail. Transport reverse does not require a formed 6-NN that itself has
transport HOLD, and Orient reverse does not read a 6-NN signed permutation of `F`. On the
four y-probes of this seed, neighbor-read reverse HOLDs with `+1,+1`
while this reverse fails; y-face fails as this face fails. On the four
z-probes of this seed, neighbor-read reverse HOLDs and face HOLDs.

Reverse neighbor-read of cyclic lex-smallest frame transport at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse fails
because cover fails at `A`. Split reverse fails because split fails at
`A`. Cover and split do not score handedness. Leftover-axis reverse fails
because leftover-axis at `A` fails from split fail. Unique signed reverse
fails because unique signed at `A` fails. Cyclic lex-largest reverse also
fails at `A` from split fail, while lex-largest Orient at `B` is `−1` and
this Orient at `B` is `+1`. Leftover-empty reverse fails because leftover
of the union at `A` is `{e_2}` and at `B` is empty: nonempty and unequal.
Leftover of `M` reverse fails because leftover of `M` at `A` is
`{e_1, e_2}` and at `B` is `{e_2, e_3}`: nonempty and unequal. Leftover
of `O` reverse fails because leftover of `O` at `A` is `{e_2, e_3}` and
at `B` is `{e_1}`: nonempty and unequal. Exist-opposite reverse of signed
`M` fails. Exist-opposite reverse of signed `O` fails. Presence of an
opposite pair in `O` HOLDs at `B` and fails at `A`. Those leftovers are
not this display.

Reverse fails.

## Theorem 3 — face from neighbor-read of cyclic lex-smallest frame transport at `τ`

Face neighbor-read of cyclic lex-smallest frame transport holds if and only if neighbor-read HOLDs at `C`
and at `D`. `neighbor-read(C)=hold` and `neighbor-read(D)=fail`. Face fails.
Witness at `C` is `(2,1,0)`. Witness at `D` is fail. Read-witness at `C`
is `(2,1,0)`. Read-witness at `D` is fail. On this member transport face
also fails and Orient face also fails, because `D` has split fail. Scalar
neighbor-read fails at `C` while neighbor-read of transport HOLDs at `C`.

Face neighbor-read of cyclic lex-smallest frame transport at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Cyclic lex-smallest Orient at `C` is `−1` and at `D`
is fail. Leftover-axis face fails because leftover-axis at `D` fails.
Unique signed face fails because unique signed at `C` fails from mixed
`±e_3`. Cover and split do not score handedness. Presence of an opposite
pair in `O` HOLDs at `C` and at `D` without cyclic columns. On the 1-axis
opposite two-site seed, cover face HOLDs while this face fails, because
that seed has cover HOLD at `A` as 2-in 1-out. The four y-probes of this
same seed give cyclic Orient `+1` at `A` and `+1` at `B`, so oriented
y-reverse HOLDs while this reverse fails; y-face fails as this face
fails. The four z-probes give neighbor-read reverse HOLD and face HOLD.
Those probe-direction readouts are not this x-probe display. Leftover-empty
face fails because leftover of the union at `C` is empty and at `D` is
`{e_2}`: nonempty and unequal. Leftover of `M` at `C` is `{e_2, e_3}` and
leftover of `M` at `D` is `{e_1, e_2}`: nonempty and unequal. Leftover of
`O` at `C` is `{e_1}` and leftover of `O` at `D` is `{e_2, e_3}`: nonempty
and unequal. Exist-opposite face of signed `M` fails. Exist-opposite face
of signed `O` fails. Cyclic lex-largest Orient at `C` is `+1` while this
Orient at `C` is `−1`.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover fails at `D` and split fails at `D`. Orient at
`D` is fail from mixed `M={+e_3, −e_3}`.

Face fails.

## What this note does not claim

- It does not select a unique outgoing or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require outgoing sides to be singletons.
- It does not sum either set.
- It does not replace neighbor-read by leftover-empty fail.
- It does not replace neighbor-read by equal `±1` Orient signs.
- It does not replace neighbor-read by nm2sfzfrm cyclic lex-smallest frame transport without a second-neighbor transport HOLD.
- It does not replace neighbor-read by scalar neighbor-read of Orient.
- It does not replace neighbor-read by equal transport bits including fail=fail.
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
- It does not reprint nm2axx axis-cover reverse hold face hold as this
  oriented display.
- It does not reprint nm2ax12x 1-in 2-out split reverse hold face hold as
  this oriented display.
- It does not reprint nm2chiralz lexicographic unsigned `o1,o2` reverse fail
  face hold with `+1,+1` as this oriented display.
- It does not reprint nm2oridetz unique signed reverse fail face fail as
  this oriented display.
- It does not reprint nm2orichz leftover-axis reverse hold face fail as
  this oriented display.
- It does not reprint nm2orionez lex-one reverse fail face hold as this
  oriented display.
- It does not reprint nm2oricyclz two-axis reverse hold face hold as this
  oriented display.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not score the y-probes or the z-probes as this letter.
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
three-axis far-face opposite seed process, neighbor-read of cyclic next/prev lex-smallest
frame transport of `(m,o_next,o_prev)` of the 1-in 2-out frame of `M` and `O`
at `t+1`, and the reverse/face bits from that neighbor-read are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three-axis far-face opposite seed `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; fail at `A` and at `D`; HOLD at `B` and at `C` |
| unique signed `m`, axis index `i`, cyclic `(o_next,o_prev)` | Theorem 1; fail at mixed `M(A)` and `M(D)`; singleton `M` and lex-smallest pair at `B` and at `C` |
| integer `det(m,o_next,o_prev)` | Theorem 1; `fail`, `1`, `-1`, `fail` |
| Orient at `τ` | Theorem 1; `fail`, `+1`, `−1`, `fail` |
| cyclic frame `F=(m,o_next,o_prev)` | Theorem 1; fail at `A` and at `D`; defined at `B` and at `C` |
| transport at `τ` | Theorem 1; `fail`, `hold`, `hold`, `fail` |
| neighbor-read at `τ` | Theorem 1; `fail`, `hold`, `hold`, `fail` |
| reverse from neighbor-read of cyclic lex-smallest frame transport at `τ` | Theorem 2; `fail` |
| face from neighbor-read of cyclic lex-smallest frame transport at `τ` | Theorem 3; `fail` |
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
| leftover of nm2chiralz lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichz leftover-axis | not this oriented display |
| leftover of nm2orionez lex-one signed `e1<e2<e3` | not this oriented display |
| leftover of cyclic lex-largest | not this oriented display |
| leftover of nm2sfzfrm cyclic lex-smallest frame transport | not this oriented display |
| leftover of scalar neighbor-read of Orient | not this oriented display |
| leftover of equal transport bits including fail=fail | not this oriented display |
| leftover of nm2oricyclz two-axis reverse hold face hold | not this oriented display |
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
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of cyclic lex-smallest frame transport of `(m,o_next,o_prev)` of the 1-in 2-out frame of `M` and `O` at `t+1` on the four x-probes of the three-axis far-face opposite seed, and reverse/face from that neighbor-read. |
| V2 | Current main has no landed neighbor-read of cyclic lex-smallest frame transport reverse/face of timed `M` and `O` on these four x-probes of the three-axis far-face opposite seed. |
| V3 | Neighbor-read reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads a formed 6-NN that itself has transport HOLD at the same `t+1` cut, reverse fails from neighbor-read fail at `A` while neighbor-read HOLDs at `B`, face fails from neighbor-read fail at `D` while neighbor-read HOLDs at `C`, scalar neighbor-read fails at `C` while neighbor-read of transport HOLDs at `C`, unique signed fails at `B` and at `C` while neighbor-read HOLDs there, y-probe reverse HOLDs while this reverse fails, z-probe reverse HOLDs and face HOLDs while this reverse fails and this face fails, cyclic lex-largest Orient at `B` is `−1` while this Orient at `B` is `+1`, and the third pair is a far-face seed at tick 0, not the two-axis child at tick 1. |
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
nm2oricyclz two-axis HOLD, does not replace Orient by
nmcover axis-cover, does not replace Orient by nm2axx axis-cover, does not
replace Orient by nm2ax12x 1-in 2-out split, does not identify this
display with the 1-axis opposite two-site seed, and does not identify it
with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2sfzfrm cyclic lex-smallest frame transport | reuse transport reverse hold and face hold | transport HOLDs reverse and face from a signed permutation of `F` without requiring a formed 6-NN that itself has transport HOLD; neighbor-read is that second-neighbor transport HOLD | ATTEMPTED |
| scalar neighbor-read of Orient | reuse same scalar Orient sign at a formed 6-NN | scalar neighbor-read HOLDs at `A`, `B`, and `D` and fails at `C` while neighbor-read of transport HOLDs at each of `A,B,C,D`; scalar face fails while this face HOLDs | ATTEMPTED |
| equal transport bits including fail=fail | score reverse/face as matching bits, including fail=fail | at `(0,-1,1)` transport fails and a formed 6-NN also fails, so equal-bit HOLDs while neighbor-read fails | ATTEMPTED |
| nm2oricycl3fz equal Orient signs | reuse Orient reverse hold and face hold | Orient reverse HOLDs from equal `±1` signs without a 6-NN signed permutation of `F`; leftover-axis face fails while this face HOLDs; unique signed fails at each probe while transport HOLDs | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face hold | unsigned reverse fails with `−1,+1` while this reverse HOLDs; unsigned face HOLDs with `+1,+1` while this face HOLDs with `−1,−1`; unsigned `o1,o2` at `B` is `(e_2,e_3)` as cyclic is `(+e_2,+e_3)` | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed fails at each of `A,B,C,D` while this Orient is `+1,+1,−1,−1`; an opposite pair in each `O` makes `|O_i|≠1` but lex-smallest still picks `+e` | ATTEMPTED |
| nm2orichz leftover-axis | reuse leftover-axis reverse and face | leftover-axis reverse HOLDs with `−1,−1` as this reverse HOLDs, but leftover-axis face fails with `+1,−1` while this face HOLDs with `−1,−1` | ATTEMPTED |
| nm2orionez lex-one | reuse lex-one reverse fail and face hold | lex-one reverse fails from `e1<e2<e3` order independent of `m` while this reverse HOLDs, and lex-one face HOLDs with `−1,−1` as this face HOLDs | ATTEMPTED |
| cyclic lex-largest | reuse same cyclic axes with `−e` if both signs | lex-largest reverse HOLDs with `−1,−1` and face HOLDs with `+1,+1`; this Orient is `+1,+1,−1,−1` | ATTEMPTED |
| nm2oricyclz two-axis HOLD | reuse two-axis reverse hold and face hold | two-axis Orient is `−1,−1,+1,+1` with reverse HOLD and face HOLD on these x-probes; this far-face seed records `(0,0,−1)` at tick 0 locking `+e_3`, while the two-axis child forms at tick 1 locking `−e_3` | ATTEMPTED |
| nm2axx axis-cover | reuse cover reverse fail and cover face fail on these x-probes | cover fails reverse and face without cyclic signed columns; neighbor-read HOLDs at `B` and at `C` | ATTEMPTED |
| nm2ax12x 1-in 2-out split | reuse split reverse fail and split face fail | split fails reverse and face without cyclic order of `Axis(M)`; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails and leftover face fails as this reverse fails and this face fails, but leftover at `B` is empty while neighbor-read HOLDs at `B`; leftover of the union at `A` is `{e_2}` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`, nonempty unequal | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse and face of `M` and of `O` | exist-opposite reverse of signed `O` HOLDs as this reverse HOLDs, but exist-opposite face of signed `O` fails while this face HOLDs; exist-opposite does not read cyclic columns | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence HOLDs at each of `A,B,C,D` without cyclic columns; leftover-axis face still fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-smallest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is `+1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member unsigned is `−1,−1,+1,+1` while this Orient is `+1,+1,−1,−1`; flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient from `+1` to `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=3`, `t(C)=4`, mixed `M(A)`, cover HOLD at `A` | different seed; second pair is a new seed, not a formed child; here `t(A)=2` and cover fails at `A` | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe reverse HOLDs while this reverse fails; y-face fails as this face fails; this letter is the four x-probes | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe reverse HOLDs and z-face HOLDs while this reverse fails and this face fails; this letter is the four x-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-smallest outgoing determinant orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face fail from mixed `M` at `A` and at `D` on the three-axis far-face opposite seed | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is three disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `+e_3` while cyclic is `(+e_3,+e_1)` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
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
nmcover axis-cover, missing identification of Orient with nm2axx axis-cover,
missing identification of Orient with nm2ax12x 1-in 2-out split, missing
identification of this seed with the 1-axis opposite two-site seed, and
missing Record identification of Orient reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three disjoint opposite seed pairs `+e_1/−e_1`,
`+e_2/−e_2`, and `+e_3/−e_3` at far-face `(0,0,−1)/(0,1,−1)` opposite the
x-probes, perpendicular step
rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ=t+1`, unsigned axis, cover as
complementary occupation of `{e_1,e_2,e_3}`, split as cover and
`|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic next/prev axes
of `Axis(M)`, lex-smallest signed outgoing letter under `+e < −e` (hence
`+e` if both signs), integer determinant sign, empty `O_next` or empty
`O_prev` as Orient fail not `UNDEFINED`, split fail as Orient fail not
`UNDEFINED`, four x-probes with `A` not a seed, second pair as a new seed not a
formed child, third pair as a new seed not a formed child, and mixed
remains a set are declared. No uniqueness of outgoing locks, no
six-neighbor lock union as the scored object, no lock-count clock, no
global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
Orient `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | unique signed incoming letter and cyclic next/prev lex-smallest outgoing letters of `Axis(M)` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports, reverse/face from those bits | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out frames. None
is taken here.

### N7 — hostile steelman

**Steelman:** Neighbor-read reverse hold and face hold are only leftover of
nm2sfzfrm transport reverse hold and face hold; leftover of scalar
neighbor-read of Orient; leftover of equal transport bits including
fail=fail; leftover of nm2oricycl3fz equal Orient signs; two-axis nm2oricyclz already answers;
cover and split already answer the member; unique signed `|O_i|=1`
already answers mixed `O`; leftover of `M` alone already answers reverse;
leftover of `O` alone already answers reverse; exist-opposite of signed
`O` already answers reverse; leftover-axis already gives the reverse HOLD;
mixed #7188 already reported the three-axis member; the third pair is only
a formed child of the two-axis seed; unique outgoing letters should be
required; cyclic lex-largest already gives HOLD bits; and unsigned
incoming axis already gives the same signs because each `M` letter is the
positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail, while this reverse HOLDs and this face HOLDs. Transport
reverse HOLDs from a signed permutation of `F` without requiring a formed
6-NN that itself has transport HOLD; neighbor-read is that second-neighbor
transport HOLD. Scalar neighbor-read of Orient HOLDs at `A`, `B`, and `D`
and fails at `C`, so scalar face fails while this face HOLDs. Equal
transport bits including fail=fail HOLDs at `(0,-1,1)` while neighbor-read
there fails. Orient reverse
HOLDs because `Orient(A)=+1` and `Orient(B)=+1`. Orient face HOLDs because
the signs are `−1` and `−1`. Cover and split HOLD reverse and face on this
member and do not score cyclic signed columns. Leftover-axis reverse HOLDs
with `−1,−1`, but leftover-axis face fails with `+1,−1` while this face
HOLDs. Lex-one reverse fails from `e1<e2<e3` order independent of `m`
while this reverse HOLDs, and lex-one face HOLDs with `−1,−1` as this
face HOLDs. Lexicographic unsigned `o1,o2` reverse fails with
`−1,+1` and face HOLDs with `+1,+1`. Unique signed `|O_i|=1` fails at each
of `A,B,C,D` while this Orient is `+1,+1,−1,−1`. Cyclic lex-largest
reverse HOLDs with `−1,−1` and face HOLDs with `+1,+1`; those signs are
not these signs. Two-axis nm2oricyclz reverse HOLDs and face HOLDs with
`−1,−1,+1,+1` on these x-probes, from a four-site seed that forms
`(0,0,−1)` at tick 1 locking `−e_3`. Presence of an opposite pair in `O`
HOLDs at each of `A,B,C,D` without cyclic columns. Leftover of `M` alone
at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`: nonempty unequal.
Leftover of `O` alone at `A` is `{e_2}` and at `B` is `{e_1}`. Unique
outgoing letters would assign `UNDEFINED` at mixed `O(A)`; this Orient is
`+1`, not `UNDEFINED`. On unique signed `O={+e_1,+e_3}` leftover is empty
while Orient is `+1`, so leftover-empty fail is not this predicate. Mixed
#7188 is a different z-symmetric process with mixed `M` and reverse fail
face fail. The second pair is a new seed, not a formed child: `(0,0,1)` is
recorded at tick 0 with lock `+e_2`, whereas the 1-axis child forms at
tick 1 with lock `+e_3`. The third pair is a new seed, not a formed child,
on the `−z` face opposite the x-probes: `(0,0,−1)` is recorded at tick 0
with lock `+e_3`, whereas the two-axis child forms at tick 1 with lock
`−e_3`. Reverse oriented frame is HOLD iff equal `±1` signs at `A` and at
`B`, not leftover of leftover-axis and not leftover of nm2oricyclz
two-axis HOLD.

### N8 — cross-cycle echo

nm2axx cover on the two-axis opposite seed reported cover HOLD at each of
the four x-probes, reverse hold, and face hold. nm2ax12x 1-in 2-out split
on that seed reported split HOLD at each of the four x-probes, reverse
hold, and face hold. nm2oricyclz cyclic lex-largest on that two-axis seed
reported Orient `−1,−1,+1,+1`, reverse hold, and face hold. On this
three-axis far-face seed, cover and split fail reverse and fail face on
the four x-probes, and cyclic lex-smallest reverse fails and face fails
from mixed `M` at `A` and at `D`; the seed is six tick-0 sites, third pair
on the `−z` face. nm2oricycl3z on the near third pair `(2,0,0)/(2,1,0)`
reported reverse fail and face fail. Unique signed outgoing letters fail
at `B` and at `C` while neighbor-read HOLDs there. Leftover axis reports
`{e_2}` at `A` and at `D` and empty leftover at `B` and at `C`, leftover
reverse fail, and leftover face fail. The four y-probes of this same seed
reported cyclic Orient `+1` at `A` from `m=−e_1` and `+1` at `B`, so
y-reverse HOLDs while this reverse fails; y-face fails from split fail at
`D`. The four z-probes of this same seed reported neighbor-read reverse
hold and face hold. This note is not those displays: it reports
neighbor-read of cyclic next/prev lex-smallest frame transport of the
1-in 2-out frame of `M` and `O` at `τ=t+1` on the three-axis far-face
opposite seed, with `t(A)=2`, `t(B)=1`, `t(C)=3`, and `t(D)=2`,
`Orient(A)=fail`, `Orient(B)=+1`, `Orient(C)=−1`, `Orient(D)=fail`,
transport fail/hold/hold/fail, neighbor-read fail/hold/hold/fail, reverse
fail, and face fail. Cover and split do not score handedness. This is not
leftover of nm2sfzfrm cyclic lex-smallest frame transport. This is not
leftover of scalar neighbor-read of Orient. This is not leftover of equal
transport bits including fail=fail.

**Gate disposition:** PASS for the neighbor-read-of-cyclic-lex-smallest-frame-transport `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
nm2sfzfrm transport without neighbor-read,” “the predicate equals scalar
neighbor-read of Orient,” “the predicate equals equal transport bits
including fail=fail,” “the predicate equals
equal Orient signs,” “the predicate equals the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals nm2chiralz lexicographic unsigned `o1,o2`
HOLD,” “the predicate equals nm2oridetz unique signed HOLD,” “the
predicate equals nm2orichz leftover-axis HOLD,” “the predicate equals
nm2orionez lex-one HOLD,” “the predicate equals cyclic lex-largest HOLD,”
“the predicate equals nm2oricyclz two-axis HOLD,” “the predicate equals
nmcover axis-cover HOLD,” “the predicate equals nm2axx axis-cover HOLD,”
“the predicate equals nm2ax12x 1-in 2-out split HOLD,” “the predicate
equals the 1-axis opposite two-site seed,” “the predicate equals nmunopp
union,” “bits are Admissibility,” “split fail is UNDEFINED,” or “empty
`O_i` is UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis far-face
opposite perp-step incoming-lock process, reads each probe's own earliest
incoming set and own outgoing dual from the record prefix at that probe's
`t+1`, reports split of the pair, reports Orient of the cyclic lex-smallest
frame, reports the cyclic frame `F=(m,o_next,o_prev)`, reports transport
of that frame along a formed 6-NN signed permutation, reports neighbor-read
of that transport HOLD at a formed 6-NN, lists new records
in `B_3(0)` between `t` and `t+1` that meet a probe's six-neighbors, and
checks Theorems 1--3. It also checks that transport is `fail` at `A` and
at `D` and `hold` at `B` and at `C`, that neighbor-read is `fail` at `A`
and at `D` and `hold` at `B` and at `C`, that reverse fails and face fails
from neighbor-read, that leftover-empty reverse and leftover-empty face
fail, that scalar neighbor-read fails at `C` while neighbor-read of
transport HOLDs at `C`, that equal transport bits including fail=fail
HOLDs at `(0,-1,1)` while neighbor-read there fails, that y-probe reverse
HOLDs while this reverse fails, that z-probe reverse HOLDs and face HOLDs
while this reverse fails and this face fails, that two-axis nm2oricyclz
on these x-probes also fails reverse and face from a four-site seed that
is not this far-face seed, that cyclic lex-largest Orient at `B` is `−1`
while this Orient at `B` is `+1`, that split fail is transport fail not
`UNDEFINED`, that empty `O_next` or empty `O_prev` is Orient fail not
`UNDEFINED`, that the 1-axis opposite two-site seed is a different member
with cover HOLD at `A` as 2-in 1-out, that leftover-empty fail is a
different predicate, that leftover of `M` alone and leftover of `O` alone
are different objects, that mixed sets remain sets, that unique-letter
Orient is `UNDEFINED` at mixed `O`, that unique signed fails at `B` and
at `C` while transport HOLDs, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not
attached, that the second pair is a new seed not a formed child, that the
third pair is a new seed not a formed child on the `−z` face, that the
y-probes and z-probes of this seed are not this letter, and that the
display is not the two-tick lock-count clock composition. No
runner cache is written.
