---
claim_id: three_axis_farface_opposite_yprobe_neighbor_read_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of the cyclic-frame transport at t+1 on the four y-probes of the three-axis far-face opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_farface_opposite_yprobe_neighbor_read_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Cyclic-Frame Transport At t+1 Reverse And Face On Four Y-Probes Of The Three-Axis Far-Face Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of cyclic-frame transport of `(m,o_next,o_prev)`
of simultaneous earliest incoming set `M` and outgoing dual `O` at each
probe's `τ=t+1`, and reverse/face from that neighbor-read, on the four
y-probes of the three-axis far-face opposite seed in `B_3(0)={n:n·n<=9}`. Same
process and y-probes as nm2ax. Transport as nm2cycfrmz.
`M`, `O`, split as nm2ax12. Orient as nm2oricycy (lex-largest cyclic).
Let `t(q)` be the
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
lex-largest vector in `O_next` (hence `−e` if both signs). `o_prev`
likewise. `Orient(q)` is the sign of the integer determinant of the 3×3
matrix with columns `m`, `o_next`, `o_prev`. If split fails, Orient fails,
not `UNDEFINED`. When split HOLDs, `F(q)=(m,o_next,o_prev)`. Transport
HOLDs at `q` if and only if split HOLDs at `q`, `Orient(q)` is `±1`, and
some formed 6-NN `r` has split HOLD, `Orient(r)` `±1`, and the 3×3 integer
matrix sending the columns of `F(q)` to the columns of `F(r)` is a signed
permutation with determinant `Orient(q)*Orient(r)`. If split or Orient
fails at `q`, transport fails, not `UNDEFINED`. Neighbor-read of that
transport HOLDs at `q` if and only if transport HOLDs at `q` and some
formed six-neighbor `r` has transport HOLD. If transport fails at `q`,
neighbor-read fails, not `UNDEFINED`. Reverse HOLDs if and only if
neighbor-read HOLDs at `A` and at `B`. Face HOLDs if and only if
neighbor-read HOLDs at `C` and at `D`. Neighbor-read of the scalar Orient
sign HOLDs only at `A` on this member and fails at `B`, `C`, and `D`.
Cover and split do not score handedness. This is not leftover of
nm2cycfrmz cyclic-frame transport reverse HOLD whose sending inspects a
signed permutation. This is not leftover of equal transport bits
including fail=fail. This is not leftover of nm2oricycy cyclic Orient
reverse fail from opposite `+1,−1` signs, not a signed-permutation
sending. This is not leftover of scalar neighbor-read of Orient. This is
not leftover of a unique nonnegative permutation sending. This is not
leftover of nm2oricycl3fz Orient reverse HOLD face HOLD from equal
signs. This is not leftover of nm2orichz leftover-axis reverse HOLD whose
face fails because C and D swap `(m,pair)` columns. This is not leftover
of nm2orionez lex-one reverse fail whose face HOLDs from `e1<e2<e3` order
independent of `m`. This is not leftover of nm2chiralz lexicographic
unsigned `o1,o2` orientation. This is not leftover of nm2oridetz unique
signed outgoing letters. This is not leftover of nm2ax axis-cover. This
is not leftover of nm2ax12 1-in 2-out split. This is not leftover of
nm2cycfrmz z-probe reverse HOLD face HOLD. This is not leftover of
nm2oricyclz two-axis HOLD. This is not leftover of leftover-of-`M` alone.
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
[`scripts/three_axis_farface_opposite_yprobe_neighbor_read_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_farface_opposite_yprobe_neighbor_read_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

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
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev
lex-largest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m` and the
lex-largest signed outgoing letter on the cyclic next and prev axes of
`Axis(M)` under `+e < −e`. When split HOLDs, `F=(m,o_next,o_prev)`.
Transport of that frame at a probe HOLDs if some formed six-neighbor has
split HOLD and Orient `±1` and the integer matrix sending the columns of
`F(q)` to the columns of `F(r)` is a signed permutation with determinant
`Orient(q)*Orient(r)`. Neighbor-read of that transport HOLDs if
transport HOLDs at the probe and some formed six-neighbor also has
transport HOLD. Reverse and face are scored on neighbor-read HOLD at
the paired probes. Neighbor-read of the scalar Orient sign is a
different readout and is not used as the object. A unique nonnegative
permutation sending is a different readout and is not used as the
object. Named signs `{+,−}` of locks are a coarser
readout and are not used as the object. A singleton unique outgoing lock
letter is a different readout and is not used as the object. Unsigned
axis units of `Axis(O)` are a different readout and are not used. Unique
signed letters requiring `|O_i|=1` are a different readout and are not
used. Opposite-pair leftover-axis orientation is a different readout and
is not used. Lex-one signed outgoing letters in axis order `e1<e2<e3`
independent of `m` are a different readout and are not used. Cyclic
lex-smallest (`+e` if both signs) is a different readout and is not used.
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
claim_type_reason: "Exact report of neighbor-read of cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 on the four y-probes of the three-axis far-face opposite seed, neighbor-read at A,B,C,D, reverse hold and face fail from neighbor-read at paired probes; uniqueness of the matching neighbor is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_farface_opposite_yprobe_neighbor_read_cyclic_frame_transport_tplus1_reverse_face
target_blocker_text: "display neighbor-read of HOLDING cyclic-frame transport reverse/face on the four y-probes of the three-axis far-face opposite seed, not leftover of nm2cycfrmz sending, not leftover of nm2frmrdy two-axis neighbor-read, not equal transport bit including fail, not scalar neighbor-read of Orient, not unique nonnegative sending, not leftover-axis, not lex-one e1<e2<e3, not unique |O_i|=1, not unsigned axis units, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 displayed; do not write neighbor-read into Admissibility, do not reduce to nm2cycfrmz sending, do not reduce to nm2frmrdy two-axis neighbor-read, do not reduce to equal transport bit including fail, do not reduce to scalar neighbor-read of Orient, do not reduce to unique nonnegative permutation sending, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-smallest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace neighbor-read by unique outgoing letters, do not replace neighbor-read by existential opposite of signed locks, do not replace neighbor-read by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 on the four y-probes of the three-axis far-face opposite seed and reverse/face from that neighbor-read; displayed, not adopted"
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
neighbor-read of cyclic-frame transport of `F=(m,o_next,o_prev)` of `M`
and `O` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the first opposite pair. `C` of the
x-probes is `(2,0,0)`, not the far-face third-pair seed. Same process and
y-probes as nm2ax.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. Site `(0,0,−1)` locks `+e_3`. Site `(0,1,−1)`
locks `−e_3`. The second pair is a new seed, not a formed child of the
first pair. The third pair is a new seed, not a formed child, and sits on
the `−z` face opposite the z-probes: on the two-axis opposite seed those
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

## Named cyclic next/prev lex-largest determinant of `M` and `O` at `τ=t+1`

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
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e. o_next is lex-largest in O_next (hence −e if both signs).
o_prev likewise.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

The outgoing pair is signed. Mixed opposite signs on one cyclic slot make
`|O_next|=2` or `|O_prev|=2`; lex-largest still picks `−e`, so Orient is
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
is a different object: it HOLDs at `A` and fails at `B`, `C`, and `D` on
this member while neighbor-read of transport HOLDs at `A`, `B`, and `C`.
A unique nonnegative permutation sending is a different object: it HOLDs
at `A` and fails at `B`, `C`, and `D`. Equal transport bits including
fail=fail is a different object: at `D` and at `(0,-1,1)` transport fails
and a formed six-neighbor also fails, so equal-bit HOLDs while
neighbor-read fails.

Reverse neighbor-read of cyclic-frame transport holds if and only if
neighbor-read HOLDs at `A` and at `B`. Face neighbor-read of cyclic-frame
transport holds if and only if neighbor-read HOLDs at `C` and at `D`.
Either side `UNDEFINED` is `UNDEFINED`. Else if both sides HOLD, reverse
or face HOLDs. Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover reverse HOLDs and cover face fails as this
reverse HOLDs and this face fails, without reading cyclic signed columns
or a 6-NN signed permutation of `F`. Identifying split reverse with this
reverse is refused: split reverse HOLDs and split face fails as these
bits, without the cyclic order of `Axis(M)` and without transport of `F`.
Identifying equal `±1` Orient signs with this reverse is refused: Orient
reverse fails with `+1,−1` while cyclic-frame transport reverse HOLDs.
Identifying leftover-empty fail with this reverse is refused:
leftover-empty reverse fails while this reverse HOLDs; leftover of the
union is empty at `A` and at `B` while Orient is a sign (`+1,−1`).
Identifying lexicographic unsigned `o1,o2` with this reverse is refused:
unsigned reverse fails with `−1,+1` as Orient reverse fails, while this
transport reverse HOLDs; unsigned `o1,o2` at `B` is `(e_2,e_3)` while
cyclic is `(+e_2,−e_3)`. Identifying nm2orionez lex-one signed
`e1<e2<e3` with this reverse is refused: lex-one reverse fails from axis
order independent of `m` while this reverse HOLDs. Identifying unique
signed `|O_i|=1` with this reverse is refused: unique signed HOLDs at `A`
and fails at `B`, so unique signed reverse fails, while this reverse
HOLDs. Identifying leftover-axis orientation with this reverse is
refused: leftover-axis reverse fails because leftover-axis at `A` fails,
while this reverse HOLDs. Identifying cyclic lex-smallest with this
reverse is refused: lex-smallest reverse HOLDs with `+1,+1` while this
Orient is `+1,−1`. Identifying nm2cycfrmz z-probe reverse HOLD face HOLD
with this reverse is refused: those four z-probes report transport HOLD
at each of `A,B,C,D` so face HOLDs, while this y-probe face fails.
Identifying two-axis nm2oricycy / nm2cycfrmy HOLD with this reverse is
refused: two-axis y-probe transport reverse HOLDs and face fails as these
bits, but that seed has four tick-0 sites, forms `(0,0,−1)` at tick 1
locking `−e_3`, and reports `O(C)={+e_1,−e_1,+e_3,−e_3}` with Orient
`+1` at `C`, while this third pair is a new seed at tick 0 locking
`+e_3/−e_3` and this `O(C)={+e_1,−e_1,+e_3}` with Orient `−1` at `C`.
Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, Orient, `F`, transport, and neighbor-read at `τ=t+1`

On this process the four y-probes form. Compare to leftover axis: leftover
at `A,B,C` is empty and leftover at `D` is `{e_2}`, leftover reverse
fails, leftover face fails, while this reverse HOLDs and this face fails.
Compare to nm2ax cover and nm2ax12 split: both HOLD reverse and FAIL face
on this member without cyclic signed columns. Compare to nm2cycfrmz on
the four z-probes of this same seed: reverse HOLDs and face HOLDs, while
this y-probe face fails. Compare to two-axis y-probe transport: reverse
HOLDs and face fails as these bits, from a four-site seed whose `O(C)`
includes `−e_3` and whose Orient at `C` is `+1`. Compare to nm2chiralz
lexicographic unsigned `o1,o2` orientation: reverse fails with `−1,+1`.
Compare to unique signed `|O_i|=1`: unique signed HOLDs at `A` and fails
at `B,C,D`. Compare to leftover-axis, which reverse fails because `A`
has no opposite pair in `O`. This display reads the cyclic next/prev
lex-largest outgoing determinant of those same timed sets, then
transports `F` as nm2cycfrmz:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {+e_3, −e_3}
O(A, τ) = {+e_2, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3}
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
o_prev(B) = −e_3
det(B) = -1
Orient(B) = −1
m(C) = +e_2
i(C) = 2
o_next(C) = +e_3
o_prev(C) = −e_1
det(C) = -1
Orient(C) = −1
m(D) fails
Orient(D) = fail
F(A) = (−e_1, +e_2, −e_3)
F(B) = (+e_1, +e_2, −e_3)
F(C) = (+e_2, +e_3, −e_1)
F(D) = fail
transport(A) = hold
transport(B) = hold
transport(C) = hold
transport(D) = fail
neighbor-read(A) = hold
neighbor-read(B) = hold
neighbor-read(C) = hold
neighbor-read(D) = fail
scalar neighbor-read(A) = hold
scalar neighbor-read(B) = fail
scalar neighbor-read(C) = fail
scalar neighbor-read(D) = fail
read-witness(A) = (0, 2, 0)
read-witness(B) = (0, 1, 1)
read-witness(C) = (0, 1, 0)
read-witness(D) = fail
witness(A) = (0, 2, 0)
witness(B) = (0, 1, 1)
witness(C) = (0, 1, 0)
witness(D) = fail
```

`A` is a seed at tick 0 with seed letter `−e_1`. Mixed remains a set:
`O(B,τ)` has three outgoing steps, and `M(D,τ)` has both `±e_3`. Unique
outgoing letters of the whole set `O` would assign `UNDEFINED` at `A`, at
`B`, at `C`, and at `D`. Unique signed `|O_i|=1` HOLDs at `A` because
`O(A)={+e_2,−e_3}` has one letter per axis, and fails at `B` from mixed
`±e_3` and at `C` from mixed `±e_1`. Split HOLDs at `A,B,C` and fails at
`D` because `Axis(M(D))={e_3}` and `Axis(O(D))={e_1}` do not cover
`{e_1,e_2,e_3}`. Cover and split do not score that cyclic lex-largest
Orient is `+1,−1,−1,fail` or that transport HOLDs at `A,B,C` and fails
at `D`. The first formed 6-NN in six-step order that transports `F` is
`C=(0,2,0)` at `A`, seed `(0,1,1)` at `B`, and seed `A=(0,1,0)` at `C`.
Uniqueness of that witness is not required. At `A`, `i=1` so
`e_next=e_2` and `e_prev=e_3`; unique signed `O_prev={−e_3}` yields
`o_prev=−e_3`. At `B`, `i=1` so `e_next=e_2` and `e_prev=e_3`; mixed
`O_prev={±e_3}` yields `o_prev=−e_3`. On the two-axis opposite seed,
`O(C)` has `−e_3` and cyclic Orient at `C` is `+1`; that seed is four
tick-0 sites, not this six-site far-face seed. Leftover-axis at `A` fails
because `O(A)` has no opposite pair. Leftover-axis at `B` is pair `+e_3`
leftover `+e_2` and that Orient is `−1`. Cyclic lex-smallest at `A` picks
the same letters as lex-largest and reports `+1`. O is not M.

On the 1-axis opposite two-site seed, y-probe `A=(0,1,0)` is still a
seed, `B` forms at tick 2, `D` forms at tick 3, cover face HOLDs, and
split fails at `D`. That is leftover of the first pair. Here `(0,0,1)`
and `(0,1,1)` are seeds of a second opposite pair on a second axis, and
`(0,0,−1)` and `(0,1,−1)` are seeds of a third opposite pair on a third
axis, on the `−z` face opposite the z-probes. On the four z-probes of
this same seed, transport HOLDs at each of `A,B,C,D`, so z-probe reverse
HOLDs and z-probe face HOLDs, while this y-probe face fails from split
fail at `D`. Those z-probes are not this letter.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,−1)` is
a seed, so it is not a new 6-NN of `A`. Site `(1,1,0)` is probe `D` and
forms at tick 2, so it is a new 6-NN of `B`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O(A)={−e_3}` from the far-face
seed `(0,1,−1)`, `O` is empty at `B` and at `C`, and `O(D)={−e_1}`. Split
fails at `t`, and Orient is fail, not UNDEFINED. Transport at `t`
therefore fails, not UNDEFINED.

Each of `A`, `B`, and `C` has a formed six-neighbor with transport HOLD.
Uniqueness of that neighbor is not required. First neighbor-read witness
in six-neighbor order: `A` reads `C=(0,2,0)`; `B` reads seed `(0,1,1)`;
`C` reads `A=(0,1,0)`; `D` has no witness because transport fails at `D`.
Those first witnesses coincide with the first signed-permutation sending
witnesses of nm2cycfrmz on these y-probes; the objects still differ:
neighbor-read does not inspect `P`. Scalar neighbor-read HOLDs only at
`A`: `B`, `C`, and `D` have no formed six-neighbor of equal Orient sign,
so scalar reverse fails and scalar face fails while neighbor-read reverse
HOLDs and neighbor-read face fails. Unique nonnegative permutation
sending HOLDs at `A` and fails at `B`, `C`, and `D`, so unique nonnegative
reverse fails while this reverse HOLDs. Equal transport bits including
fail=fail HOLDs at `D` and at `(0,-1,1)` because those sites' transport
fails and a formed six-neighbor also fails, while neighbor-read at those
sites fails, not `UNDEFINED`.

## Theorem 2 — reverse from neighbor-read of cyclic-frame transport at `τ`

Reverse neighbor-read of cyclic-frame transport holds if and only if
neighbor-read HOLDs at `A` and at `B`. `neighbor-read(A)=hold` and
`neighbor-read(B)=hold`. Reverse HOLDs. This is HOLD iff both
neighbor-reads HOLD, not leftover of nm2cycfrmz cyclic-frame transport
sending, not leftover of equal transport bits including fail=fail, not
leftover of nm2oricycy cyclic Orient equal signs, not leftover of
scalar neighbor-read, not leftover of a unique nonnegative permutation
sending, not leftover of nm2chiralz lexicographic unsigned `o1,o2`, not
leftover of nm2oridetz unique signed outgoing letters, not leftover of
nm2orichz leftover-axis, not leftover of nm2orionez lex-one, not leftover
of nm2ax axis-cover, not leftover of nm2ax12 1-in 2-out split, not
leftover of nm2cycfrmz, not leftover of nm2oricyclz two-axis HOLD, not
leftover-empty fail, and not exist-opposite. On this member Orient reverse
fails with `+1,−1` while neighbor-read reverse HOLDs.

Reverse neighbor-read of cyclic-frame transport at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Leftover-axis reverse fails because leftover-axis at `A` fails, while this
reverse HOLDs. Lexicographic unsigned reverse fails because unsigned
`Orient(A)=−1` and `Orient(B)=+1`. Unique signed reverse fails because
unique signed at `B` fails. Lex-one signed reverse fails from
`e1<e2<e3` order independent of `m`. Cyclic lex-smallest reverse HOLDs
with `+1,+1`. Two-axis y-probe transport reverse HOLDs as this reverse
HOLDs, from a different four-site seed. Leftover-empty reverse fails
because leftover of the union is empty at `A` and at `B`. Leftover of `M`
reverse HOLDs because leftover of `M` at `A` and at `B` are both
`{e_2, e_3}`, without reading `F`. Leftover of `O` reverse HOLDs because
leftover of `O` at `A` and at `B` are both `{e_1}`. Exist-opposite reverse
of signed `M` HOLDs because `−e_1` in `M(A)` meets `+e_1` in `M(B)`.
Exist-opposite reverse of signed `O` HOLDs because `−e_3` in `O(A)` meets
`+e_3` in `O(B)`. Presence of an opposite pair in `O` fails at `A`. Those
leftovers are not this display.

Reverse HOLDs.

## Theorem 3 — face from neighbor-read of cyclic-frame transport at `τ`

Face neighbor-read of cyclic-frame transport holds if and only if
neighbor-read HOLDs at `C` and at `D`. `neighbor-read(C)=hold` and
`neighbor-read(D)=fail`. Face fails. Witness at `C` is `A=(0,1,0)`.
Witness at `D` is fail. On this member Orient face fails because Orient
at `D` fails. nm2cycfrmz z-probe face HOLDs on this same seed, while this
y-probe face fails. Scalar neighbor-read face fails as this face fails,
from a different object: equal Orient signs, not a neighbor transport
HOLD bit.

Face neighbor-read of cyclic-frame transport at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Cyclic lex-largest oriented face fails because Orient
at `D` fails. Leftover-axis face fails. Unique signed face fails because
unique signed at `C` fails from mixed `±e_1`. Cover and split do not
score handedness. Presence of an opposite pair in `O` HOLDs at `C` and at
`D` without cyclic columns, while this face fails. On the 1-axis opposite
two-site seed, cover face HOLDs while split face fails at `D`, and Orient
at `D` is fail, not UNDEFINED. This three-axis far-face member is not
leftover of that 1-axis cover face HOLD: here cover fails at `D`. The
four z-probes of this same seed give transport HOLD at each of `A,B,C,D`,
so z-face HOLDs while this y-face fails. The four x-probes give oriented
reverse fail and oriented face fail, and x-probe `C` is `(2,0,0)`, not
the far-face third-pair seed. Those probe-direction readouts are not this
y-probe display. Leftover-empty face fails because leftover of the union
at `D` is `{e_2}` and leftover-empty fail scores empty leftover as fail.
Leftover of `M` at `C` is `{e_1, e_3}` and leftover of `M` at `D` is
`{e_1, e_2}`: nonempty and unequal. Leftover of `O` at `C` is `{e_2}` and
leftover of `O` at `D` is `{e_2, e_3}`: nonempty and unequal.
Exist-opposite face of signed `M` fails. Exist-opposite face of signed
`O` HOLDs because `+e_1` in `O(C)` meets `−e_1` in `O(D)`, while this
face fails. Two-axis y-probe transport face fails as this face fails,
from a four-site seed whose `O(C)` includes `−e_3`.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover fails at `D` and split fails at `D`. Orient at
`D` is fail because split fails, not UNDEFINED.

Face fails.

## What this note does not claim

- It does not replace neighbor-read of transport by nm2cycfrmz signed-permutation sending.
- It does not replace neighbor-read by equal transport bits including fail=fail.
- It does not replace neighbor-read of transport by neighbor-read of the scalar Orient sign.
- It does not replace neighbor-read of transport by a unique nonnegative permutation sending.
- It does not require a unique formed six-neighbor witness.
- It does not reprint nm2oricycy cyclic Orient reverse fail as this neighbor-read.
- It does not select a unique outgoing or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require outgoing sides to be singletons.
- It does not sum either set.
- It does not replace transport by leftover-empty fail.
- It does not replace transport by equal `±1` Orient signs.
- It does not replace Orient by leftover of `M` alone.
- It does not replace Orient by leftover of `O` alone.
- It does not replace Orient by existential opposite of signed locks.
- It does not replace Orient by presence of an opposite pair in `O`.
- It does not replace Orient by lexicographic unsigned `o1,o2` orientation.
- It does not replace Orient by unique signed `|O_i|=1` letters.
- It does not replace Orient by leftover-axis orientation.
- It does not replace Orient by nm2orionez lex-one signed `e1<e2<e3`.
- It does not replace Orient by cyclic lex-smallest (`+e` if both signs).
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
- It does not reprint nm2ax axis-cover reverse hold face fail as this
  oriented display.
- It does not reprint nm2ax12 1-in 2-out split reverse hold face fail as
  this oriented display.
- It does not reprint nm2cycfrmz z-probe reverse hold face hold as this
  oriented display.
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
three-axis far-face opposite seed process, neighbor-read of cyclic-frame transport of
`(m,o_next,o_prev)` of `M` and `O` at `t+1`, and the reverse/face bits
from that neighbor-read are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three-axis far-face opposite seed `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; HOLD at `A,B,C`; fail at `D` |
| unique signed `m`, axis index `i`, cyclic `(o_next,o_prev)` | Theorem 1; singleton `M` at `A,B,C`; mixed `M` at `D` |
| integer `det(m,o_next,o_prev)` | Theorem 1; `1`, `-1`, `-1`, fail |
| Orient at `τ` | Theorem 1; `+1`, `−1`, `−1`, fail |
| cyclic frame `F=(m,o_next,o_prev)` | Theorem 1; defined at `A,B,C`; fail at `D` |
| transport at `τ` | Theorem 1; `hold` at `A,B,C`; `fail` at `D`; nm2cycfrmz leftover |
| neighbor-read of transport at `τ` | Theorem 1; `hold` at `A,B,C`; `fail` at `D` |
| scalar neighbor-read of Orient | Theorem 1; HOLD at `A`, fail at `B,C,D`; not this letter |
| reverse from neighbor-read of cyclic-frame transport at `τ` | Theorem 2; `hold` |
| face from neighbor-read of cyclic-frame transport at `τ` | Theorem 3; `fail` |
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
| leftover of nm2cycfrmz z-probe reverse hold face hold | not this oriented display |
| leftover of nm2cycfrmz cyclic-frame transport sending | not this neighbor-read |
| leftover of nm2frmrdy two-axis neighbor-read | not this neighbor-read |
| leftover of equal transport bits including fail=fail | not this neighbor-read |
| leftover of scalar neighbor-read of Orient | not this neighbor-read |
| leftover of unique nonnegative permutation sending | not this neighbor-read |
| leftover of nm2chiralz lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichz leftover-axis | not this oriented display |
| leftover of nm2orionez lex-one signed `e1<e2<e3` | not this oriented display |
| leftover of cyclic lex-smallest | not this oriented display |
| leftover of nm2oricyclz two-axis reverse hold face hold | not this oriented display |
| leftover of opposite-pair presence in `O` | not this oriented display |
| z-probe or x-probe transport on this seed | not this letter |
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
| V1 | It answers the first-display question: neighbor-read of cyclic-frame transport of `(m,o_next,o_prev)` of `M` and `O` at `t+1` on the four y-probes of the three-axis far-face opposite seed, and reverse/face from that neighbor-read. |
| V2 | Current main has no landed neighbor-read of cyclic-frame-transport reverse/face of timed `M` and `O` on these four y-probes of the three-axis far-face opposite seed. |
| V3 | Neighbor-read reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the transport HOLD bit at a formed six-neighbor at the same `t+1` cut on the six-site far-face seed, reverse HOLDs and face fails while scalar neighbor-read reverse fails and scalar face fails, unique nonnegative sending HOLDs at `A` and fails at `B` so unique nonnegative reverse fails, equal transport bits including fail=fail HOLDs at `D` where this neighbor-read fails, nm2frmrdy is the four-site two-axis leftover, and nm2cycfrmz sending inspects `P` which this neighbor-read does not. |
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
does not replace Orient by cyclic lex-smallest, does not replace Orient by
nm2oricyclz two-axis HOLD, does not replace Orient by
nmcover axis-cover, does not replace Orient by nm2ax axis-cover, does not
replace Orient by nm2ax12 1-in 2-out split, does not replace transport by
nm2cycfrmz z-probe reverse HOLD face HOLD, does not identify this
display with the 1-axis opposite two-site seed, and does not identify it
with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2cycfrmz cyclic-frame transport sending | reuse signed-permutation sending of `F(q)` to `F(r)` | sending inspects `P`; this neighbor-read reads only the transport HOLD bit at a formed 6-NN. On this member the four probe bits agree, but at `D` and at `(0,-1,1)` equal-bit HOLDs while neighbor-read fails | ATTEMPTED |
| nm2frmrdy two-axis neighbor-read | reuse neighbor-read reverse hold and face fail on the two-axis opposite seed | two-axis leftover is four tick-0 sites; this member records a third opposite pair at tick 0 on the `−z` far face | ATTEMPTED |
| equal transport bits including fail=fail | HOLD if some formed 6-NN has the same transport bit | at `D` and at `(0,-1,1)` transport fails and a formed 6-NN also fails, so equal-bit HOLDs while neighbor-read fails, not UNDEFINED | ATTEMPTED |
| scalar neighbor-read of Orient | reuse equal Orient sign at some formed 6-NN | scalar HOLDs at `A` and fails at `B,C,D`; scalar reverse fails while this reverse HOLDs | ATTEMPTED |
| unique nonnegative permutation sending | require a unique sending with no minus signs | unique nonnegative sending HOLDs at `A` and fails at `B,C,D`; unique nonnegative reverse fails while this reverse HOLDs; uniqueness is not required | ATTEMPTED |
| nm2oricycl3fz equal Orient signs | reuse Orient reverse hold and face hold | Orient reverse fails with `+1,−1` while neighbor-read reverse HOLDs; equal signs do not read a 6-NN signed permutation of `F` | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face hold | unsigned reverse fails with `−1,+1` while this reverse HOLDs; unsigned `o1,o2` at `B` is `(e_2,e_3)` while cyclic is `(+e_2,−e_3)` | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed HOLDs at `A` and fails at `B`; unique signed reverse fails while this reverse HOLDs | ATTEMPTED |
| nm2orichz leftover-axis | reuse leftover-axis reverse and face | leftover-axis reverse fails at `A` because `O(A)` has no opposite pair, while this reverse HOLDs | ATTEMPTED |
| nm2orionez lex-one | reuse lex-one reverse fail and face hold | lex-one reverse fails from `e1<e2<e3` order independent of `m` while this reverse HOLDs | ATTEMPTED |
| cyclic lex-smallest | reuse same cyclic axes with `+e` if both signs | lex-smallest reverse HOLDs with `+1,+1`; this Orient is `+1,−1` | ATTEMPTED |
| nm2oricyclz two-axis HOLD | reuse two-axis reverse hold and face hold | two-axis y-probe transport reverse HOLDs and face fails as these bits, from a four-site seed whose `O(C)` includes `−e_3` and whose Orient at `C` is `+1` | ATTEMPTED |
| nm2cycfrmz z-probe transport | reuse z-probe reverse hold and face hold | those four z-probes report transport HOLD at each of `A,B,C,D` so face HOLDs, while this y-probe face fails | ATTEMPTED |
| nm2ax axis-cover | reuse cover reverse hold and cover face fail on these y-probes | cover HOLDs reverse and fails face without cyclic signed columns | ATTEMPTED |
| nm2ax12 1-in 2-out split | reuse split reverse hold and split face fail | split HOLDs reverse and fails face without cyclic order of `Axis(M)`; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails while this reverse HOLDs; leftover of the union is empty at `A` and at `B` while Orient is a sign | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and at `B` are both `{e_2,e_3}` without reading `F` | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and at `B` are both `{e_1}` without reading `F` | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse and face of `M` and of `O` | exist-opposite reverse of signed `O` HOLDs as this reverse HOLDs, and exist-opposite face of signed `O` HOLDs while this face fails; exist-opposite does not read cyclic columns | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence fails at `A` while this reverse HOLDs; pair-presence HOLDs at `C` and at `D` while this face fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-largest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(B,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient at `B` is `−1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | unsigned at `A` is `−1` while signed `m=−e_1` reports `+1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `D` is not 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(B)=2`, `t(D)=3`, cover face hold | different seed; second pair is a new seed, not a formed child; here `t(B)=1` and cover fails at `D` | ATTEMPTED |
| z-probe transport | score the four z-probes on this seed | z-probe reverse HOLDs and z-probe face HOLDs; this letter is the four y-probes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe `C` is `(2,0,0)`, not the far-face third-pair seed; this letter is the four y-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-largest outgoing determinant orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse hold and face fail on the three-axis far-face opposite seed | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is three disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `+e_3` while cyclic is `(+e_3,−e_1)` | ATTEMPTED |
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
Orient with cyclic lex-smallest, missing identification of Orient with
nmcover axis-cover, missing identification of Orient with nm2ax axis-cover,
missing identification of Orient with nm2ax12 1-in 2-out split, missing
identification of transport with nm2cycfrmz z-probe reverse HOLD face HOLD,
missing identification of this seed with the 1-axis opposite two-site seed, and
missing Record identification of Orient reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three disjoint opposite seed pairs `+e_1/−e_1`,
`+e_2/−e_2`, and `+e_3/−e_3` at far-face `(0,0,−1)/(0,1,−1)` opposite the
z-probes, perpendicular step
rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ=t+1`, unsigned axis, cover as
complementary occupation of `{e_1,e_2,e_3}`, split as cover and
`|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic next/prev axes
of `Axis(M)`, lex-largest signed outgoing letter under `+e < −e` (hence
`−e` if both signs), integer determinant sign, empty `O_next` or empty
`O_prev` as Orient fail not `UNDEFINED`, split fail as Orient fail not
`UNDEFINED`, four y-probes with seed `A`, second pair as a new seed not a
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
| per element | neighbor-read of the cyclic-frame transport HOLD bit at a formed 6-NN | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports, reverse/face from those bits | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for neighbor-read of
cyclic-frame transport reverse/face, a formation-rate rule, and a
physical selector among 1-in 2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Neighbor-read reverse hold and face fail are only leftover of
nm2cycfrmz cyclic-frame transport sending, or of equal transport bits
including fail=fail, or of nm2oricycy cyclic Orient, or of neighbor-read
of the scalar Orient sign, or of cover and split; two-axis y-probe
neighbor-read already answers; unique nonnegative sending already HOLDs
at `A`; leftover-axis already answers reverse; unique signed `|O_i|=1`
already answers mixed `O`; leftover of `M` alone already answers reverse;
leftover of `O` alone already answers reverse; exist-opposite of signed
`O` already answers reverse; mixed #7188 already reported the three-axis
member; the third pair is only a formed child of the two-axis seed; unique
outgoing letters should be required; cyclic lex-smallest already gives
HOLD bits; and unsigned incoming axis already gives the same signs because
each `M` letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail,
while this reverse HOLDs. Neighbor-read reverse HOLDs because
neighbor-read HOLDs at `A` and at `B`. Neighbor-read face fails because
neighbor-read fails at `D` from transport fail. Scalar neighbor-read of
Orient HOLDs only at `A` and fails at `B`, `C`, and `D`, so scalar reverse
fails. Unique nonnegative permutation sending HOLDs at `A` and fails at
`B`, `C`, and `D`, so unique nonnegative reverse fails. Equal transport
bits including fail=fail HOLDs at `D` while neighbor-read fails. Orient
reverse fails because `Orient(A)=+1` and `Orient(B)=−1`, while
neighbor-read reverse HOLDs. Cover and split HOLD reverse and fail face
on this member and do not score cyclic signed columns. Leftover-axis
reverse fails at `A` because `O(A)` has no opposite pair, while this
reverse HOLDs. Lex-one reverse fails from `e1<e2<e3` order independent of
`m` while this reverse HOLDs. Lexicographic unsigned `o1,o2` reverse fails
with `−1,+1`. Unique signed `|O_i|=1` HOLDs at `A` and fails at `B`, so
unique signed reverse fails. Cyclic lex-smallest reverse HOLDs with
`+1,+1`; this Orient is `+1,−1`. nm2cycfrmz reports transport HOLD at each
z-probe so z-face HOLDs, while this y-probe face fails. Two-axis y-probe
neighbor-read reverse HOLDs and face fails as these bits, from a
four-site seed whose `O(C)` includes `−e_3` and whose Orient at `C` is
`+1`. Presence of an opposite pair in `O` fails at `A`. Leftover of `M`
alone at `A` and at `B` are both `{e_2,e_3}`. Leftover of `O` alone at `A`
and at `B` are both `{e_1}`. Unique outgoing letters would assign
`UNDEFINED` at mixed `O(B)`; this Orient at `B` is `−1`, not `UNDEFINED`.
Unsigned incoming axis at `A` is `−1` while signed `m=−e_1` reports `+1`.
Mixed #7188 is a different z-symmetric process with mixed `M` and reverse
fail face fail. The second pair is a new seed, not a formed child. The
third pair is a new seed, not a formed child, on the `−z` face opposite
the z-probes: `(0,0,−1)` is recorded at tick 0 with lock `+e_3`, whereas
the two-axis child forms at tick 1 with lock `−e_3`. Reverse neighbor-read
of cyclic-frame transport is HOLD iff neighbor-read HOLDs at `A` and at
`B`, not leftover of equal Orient signs and not leftover of nm2cycfrmz
sending.

### N8 — cross-cycle echo

nm2ax cover on the two-axis opposite y-probes reported cover HOLD reverse
and cover fail face. nm2ax12 1-in 2-out split on that seed reported split
HOLD reverse and split fail face. Two-axis y-probe cyclic-frame transport
reported reverse hold and face fail. On this three-axis far-face seed,
cover and split still HOLD reverse and fail face, but `O(C)` lacks `−e_3`
and Orient at `C` is `−1`, not `+1`; the seed is different: six tick-0
sites, third pair on the `−z` face. nm2cycfrmz on the four z-probes of
this same seed reported transport HOLD at each of `A,B,C,D`, reverse hold,
and face hold. nm2chiralz lexicographic unsigned `o1,o2` on this seed
reported reverse fail. Unique signed outgoing letters on these y-probes
HOLD at `A` and fail at `B`. Leftover-axis reverse fails at `A`. Leftover
axis leftover-empty reverse fails while this reverse HOLDs. This note is
not those displays: it reports neighbor-read of cyclic-frame transport of
`(m,o_next,o_prev)` of `M` and `O` at `τ=t+1` on the four y-probes of the
three-axis far-face opposite seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`, and
`t(D)=2`, `transport(A)=hold`, `transport(B)=hold`, `transport(C)=hold`,
`transport(D)=fail`, `neighbor-read(A)=hold`, `neighbor-read(B)=hold`,
`neighbor-read(C)=hold`, `neighbor-read(D)=fail`, reverse hold, and face
fail, while scalar neighbor-read fails at `B,C,D`. Cover and split do not
score handedness.

**Gate disposition:** PASS for the neighbor-read of cyclic-frame-transport
`t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the predicate
equals the named sign,” “the predicate equals the unique singleton lock
vector,” “the predicate equals six-neighbor lock union,” “the predicate
equals leftover-empty fail,” “the predicate equals leftover of `M`
alone,” “the predicate equals leftover of `O` alone,” “the predicate
equals exist-opposite HOLD,” “the predicate equals opposite-pair presence
in `O`,” “the predicate equals nm2chiralz lexicographic unsigned `o1,o2`
HOLD,” “the predicate equals nm2oridetz unique signed HOLD,” “the
predicate equals nm2orichz leftover-axis HOLD,” “the predicate equals
nm2orionez lex-one HOLD,” “the predicate equals cyclic lex-smallest HOLD,”
“the predicate equals nm2oricycy cyclic Orient HOLD,” “the predicate
equals nm2cycfrmz cyclic-frame transport sending HOLD,” “the predicate
equals nm2frmrdy two-axis neighbor-read HOLD,” “the predicate equals
equal transport bits including fail=fail HOLD,” “the predicate equals
scalar neighbor-read of Orient HOLD,” “the predicate equals unique
nonnegative permutation sending HOLD,” “the predicate equals nmcover
axis-cover HOLD,” “the predicate equals nm2ax axis-cover HOLD,” “the
predicate equals nm2ax12 1-in 2-out split HOLD,” “the predicate equals
nm2cycfrmz z-probe reverse HOLD face HOLD,” “the predicate equals the
1-axis opposite two-site seed,” “the predicate equals nmunopp union,”
“bits are Admissibility,” “split fail is UNDEFINED,” or “empty `O_i` is
UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis far-face
opposite perp-step incoming-lock process, reads each probe's own earliest
incoming set and own outgoing dual from the record prefix at that probe's
`t+1`, reports split of the pair, reports the cyclic frame
`F=(m,o_next,o_prev)`, reports Orient as nm2oricycy lex-largest cyclic,
reports transport as nm2cycfrmz by a signed-permutation sending to some
formed six-neighbor, reports neighbor-read of that transport HOLD bit at
a formed six-neighbor, lists new records in `B_3(0)` between `t` and
`t+1` that meet a probe's six-neighbors, and checks Theorems 1--3. It
also checks that neighbor-read HOLDs at `A,B,C` and fails at `D` while
scalar neighbor-read fails at `B,C,D`, that reverse HOLDs and face fails
from neighbor-read while scalar reverse fails and scalar face fails, that
unique nonnegative permutation sending HOLDs at `A` and fails at `B,C,D`,
that leftover-axis reverse fails and lex-one reverse fails from
`e1<e2<e3` order independent of `m`, that transport fail is neighbor-read
fail not `UNDEFINED`, that equal transport bits including fail=fail HOLDs
at `D` and at `(0,-1,1)` while neighbor-read fails there, that empty
`O_next` or empty `O_prev` is Orient fail not `UNDEFINED`, that the
1-axis opposite two-site seed is a different member with cover face HOLD,
that leftover-empty fail is a different predicate, that leftover of `M`
alone and leftover of `O` alone are different objects, that mixed sets
remain sets, that the construction does not sum, that a formation member
from already-recorded six-neighbor locks is not attached, that the second
pair is a new seed not a formed child, that the third pair is a new seed
not a formed child, that the two-axis opposite seed is a different
four-site member, that the z-probes and x-probes of this seed are not
this letter, and that the display is not the two-tick lock-count clock
composition. No runner cache is written.
