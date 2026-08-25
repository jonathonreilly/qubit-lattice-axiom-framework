---
claim_id: three_axis_farface_opposite_xprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of cyclic lex-smallest frame transport at t+1 versus t+2 on the four x-probes of the three-axis far-face opposite seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_farface_opposite_xprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Cyclic Lex-Smallest Frame Transport Freeze t+1 Versus t+2 Reverse And Face On Four X-Probes Of The Three-Axis Far-Face Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of cyclic lex-smallest frame transport of `(m,o_next,o_prev)` of simultaneous
earliest incoming set `M` and outgoing dual `O` at each probe's `τ1=t+1`
and `τ2=t+2`, reverse/face from that neighbor-read at each cut, and composition
of neighbor-read, on the four x-probes of the three-axis far-face opposite seed in
`B_3(0)={n:n·n<=9}`. Same process and x-probes as nm2ax. `M`, `O`, split
as nm2ax12. Orient as nm2oricyccx (lex-smallest cyclic). Transport as
nm2sfzfrm at each cut. Neighbor-read as nm2sfzrdx at each cut. Let `t(q)` be the formation tick of probe `q`.
Cuts are local: `τ1=t+1`, `τ2=t+2`. There is no global T. Do not score τ=t. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds
are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the
set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). When split HOLDs, `m` is unique in
`M`. Let `i` in `{1,2,3}` be the axis index of `m`. `e_next = e_{i+1}`
with `3+1→1`. `e_prev = e_{i-1}` with `1−1→3`. `O_next = O ∩ {±e_next}`.
`O_prev = O ∩ {±e_prev}`. If either empty, Orient fails, not `UNDEFINED`.
Order `+e < −e`. `o_next` is the lex-smallest vector in `O_next` (hence
`+e` if both signs). `o_prev` likewise. `Orient(q,τ)` is the sign of the
integer determinant of the 3×3 matrix with columns `m`, `o_next`,
`o_prev`. If split fails, Orient fails, not `UNDEFINED`. When split
HOLDs, `F(q,τ)=(m,o_next,o_prev)` is an oriented lattice frame: a LIVE
three-axis 1-in 2-out triple. Transport as nm2sfzfrm at each cut.
Transport HOLDs at `q` at a cut if and only if split HOLDs at `q`,
`Orient(q)` is `±1`, and some formed six-neighbor `r` has split HOLD,
`Orient(r)` `±1`, and the 3×3 integer matrix sending the columns of
`F(q)` to the columns of `F(r)` is a signed permutation with determinant
`Orient(q)Orient(r)`, with `M`, `O`, and `F` read at that site's
`t+offset`. If split or Orient fails at `q`, transport fails, not
`UNDEFINED`. Neighbor-read HOLDs at `q` at a cut if and only if transport
HOLDs at `q` and some formed six-neighbor `r` has transport HOLD, with
transport read at that site's `t+offset`. If transport fails at `q`,
neighbor-read fails, not `UNDEFINED`. Reverse HOLDs if and only if neighbor-read HOLDs at `A` and at
`B` at that cut. Face HOLDs if and only if neighbor-read HOLDs at `C` and at
`D` at that cut. Composition HOLDs if and only if neighbor-read at `τ1` equals
neighbor-read at `τ2` at `A,B,C,D`. Neighbor-read of the scalar Orient sign
HOLDs at `A`, `B`, and `D` and fails at `C` on this member, including #7477
same-lock as a different seed whose face transport fails, and including
LIVE three-axis as the frame itself rather than a scalar. Cover and split
do not score handedness. This is not leftover of nm2sfzfrm cyclic-frame
transport at `t+1` alone. This is not leftover of nm2sfzrdx neighbor-read
at `t+1` alone. This is not leftover of nm2sfzfrmt2 transport freeze
without neighbor-read. This is not leftover of nm2oricycx cyclic Orient
reverse HOLD whose bits are equal `±1` signs, not a signed-permutation
sending. This is not leftover of nm2simt2x simultaneous `M` and `O` freeze.
This is not leftover of scalar neighbor-read of Orient. This is not leftover
of equal transport bits including fail=fail. This is not
leftover of a unique nonnegative permutation sending. This is not leftover
of nm2orichx leftover-axis reverse HOLD whose face fails because C and D
swap `(m,pair)` columns. This is not leftover of nm2orionex lex-one reverse
fail whose face HOLDs from `e1<e2<e3` order independent of `m`. This is
not leftover of nm2chiralx lexicographic unsigned `o1,o2` orientation.
This is not leftover of nm2oridetx unique signed outgoing letters. This
is not leftover of nm2ax axis-cover. This is not leftover of nm2ax12
1-in 2-out split. This is not leftover of leftover-of-`M` alone. This is
not leftover of leftover-of-`O` alone. This is not leftover-empty fail of
leftover axis. This is not leftover of nmunopp union. This is not leftover
of nmt2opp `M` frozen at `t`. This is not leftover of nmot2opp two-tick
composition. This is not leftover of nmoutopp untimed eventual-`O`. This
is not leftover of mixed #7188 fail/fail. This is not leftover of the
1-axis opposite two-site seed. This is not leftover of the same-lock
two-site seed. This is not leftover of the two-axis opposite seed of
nm2cycfrmz. The second pair is a new seed, not a formed child. The third
pair is a new seed, not a formed child. Uniqueness is not required. Mixed
remains a set. Displayed, not adopted.
Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_farface_opposite_xprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/three_axis_farface_opposite_xprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cuts
`τ1=t+1` and `τ2=t+2`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev
lex-smallest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m` and the
lex-smallest signed outgoing letter on the cyclic next and prev axes of
`Axis(M)` under `+e < −e`. When split HOLDs, `F=(m,o_next,o_prev)` is
that LIVE three-axis frame. Transport is existential: some formed
six-neighbor hosts a split-HOLDING frame whose columns are a signed
permutation of the source columns with determinant the product of the
two Orient signs. Neighbor-read of that transport HOLDs if transport HOLDs
at the probe and some formed six-neighbor also has transport HOLD. Reverse
and face are scored on neighbor-read HOLD at the paired probes at each
cut. Composition is equality of those four neighbor-read reports across
the two cuts. Neighbor-read of the scalar Orient sign is a different
readout and is not used as the object. A unique nonnegative permutation
sending is a different readout and is not used as the object. Named
signs `{+,−}` of locks are a coarser readout and are not used as the
object. A singleton unique outgoing lock letter is a different readout
and is not used as the object. Unsigned axis units of `Axis(O)` are a
different readout and are not used. Unique signed letters requiring
`|O_i|=1` are a different readout and are not used. Opposite-pair
leftover-axis orientation is a different readout and is not used.
Lex-one signed outgoing letters in axis order `e1<e2<e3` independent of
`m` are a different readout and are not used. Cyclic lex-largest (`−e`
if both signs) is a different readout and is not used. Existential
opposite of signed locks is a different readout and is not used.
Axis-cover without the frame sign is a different readout and is not
used. 1-in 2-out split without the frame sign is a different readout and
is not used. Equal `±1` Orient signs without a sending matrix are a
different readout and are not used. Leftover-empty fail of unsigned
leftover axis sets is a different readout and is not used. A `Z^3` sum
of those locks is a different readout and is not used. Occupancy of
sites is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of cyclic lex-smallest frame transport of (m,o_next,o_prev) of M and O at t+1 versus t+2 on the four x-probes of the three-axis far-face opposite seed, transport and neighbor-read at A,B,C,D at each cut, reverse fail and face fail at each cut from neighbor-read, composition hold; uniqueness of the sending neighbor is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_farface_opposite_xprobe_neighbor_read_cyclic_lex_smallest_frame_transport_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display neighbor-read of cyclic lex-smallest frame transport freeze t+1 versus t+2 reverse/face composition on the four x-probes of the three-axis far-face opposite seed, not transport without neighbor-read, not scalar neighbor-read of Orient, not unique nonnegative sending, not leftover of nm2sfzrdx t+1 alone, not leftover of nm2sfzfrmt2, not leftover of nm2simt2x"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of cyclic lex-smallest frame transport of (m,o_next,o_prev) of M and O at t+1 versus t+2 displayed; do not write the bits into Admissibility, do not reduce to nm2sfzfrm t+1 alone, do not reduce to nm2sfzrdx t+1 alone, do not reduce to nm2sfzfrmt2 transport freeze without neighbor-read, do not reduce to nm2simt2x M-and-O freeze, do not reduce to scalar neighbor-read of Orient, do not reduce to equal transport bits including fail=fail, do not reduce to unique nonnegative permutation sending, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-largest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace neighbor-read by unique outgoing letters, do not replace neighbor-read by existential opposite of signed locks, do not replace neighbor-read by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of cyclic lex-smallest frame transport of (m,o_next,o_prev) of M and O at t+1 versus t+2 on the four x-probes of the three-axis far-face opposite seed, reverse/face at each cut, and composition; displayed, not adopted"
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
neighbor-read of cyclic-frame transport of `F=(m,o_next,o_prev)` of `M` and `O` is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is not a seed: it forms at tick 2 locking `{+e_3,−e_3}`.
`C` is `(2,0,0)`, not the far-face third-pair seed. Same process and
x-probes as nm2ax.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. Site `(0,0,−1)` locks `+e_3`. Site `(0,1,−1)`
locks `−e_3`. The second pair is a new seed, not a formed child of the
first pair. The third pair is a new seed, not a formed child, and sits on
the `−z` face opposite the x-probes: on the two-axis opposite seed those
sites form at tick 1 locking `−e_3`. This seed is not the two-axis
opposite seed of nm2cycfrmz. This seed is not the 1-axis opposite two-site seed
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

## Named cyclic lex-smallest frame transport of `(m,o_next,o_prev)` at `τ1` and `τ2`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
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

Cyclic frame and transport at the same cut:

```text
When split HOLDs, F(q)=(m, o_next, o_prev).
Transport HOLDs at q iff split HOLDs, Orient(q) is ±1,
and some formed 6-NN r has split HOLD, Orient(r) ±1,
and the 3×3 integer matrix P sending the columns of F(q)
to the columns of F(r) (F(r)=F(q)P) is a signed permutation
with det(P)=Orient(q)Orient(r).
If split or Orient fails at q, transport fails, not UNDEFINED.
UNDEFINED if M or O is UNDEFINED.
Uniqueness of r is not required.

Neighbor-read HOLDs at q iff transport(q) HOLDs
and some formed 6-NN r has transport(r) HOLD.
If transport fails at q, neighbor-read fails, not UNDEFINED.
UNDEFINED if transport is UNDEFINED.
Uniqueness of r is not required.
```

Neighbor-read of the scalar Orient sign HOLDs at `q` if and only if
`Orient(q)` is `±1` and some formed six-neighbor has the same sign. That
is a different object: it HOLDs at `A`, `B`, and `D` and fails at `C` on
this member while neighbor-read of transport fails at `A` and at `D` and HOLDs at `B` and at `C`.
Equal transport bits including fail=fail is a different object: at
`(0,-1,1)` transport fails and a formed six-neighbor also fails, so
equal-bit HOLDs while neighbor-read fails. A unique
nonnegative permutation sending is a different object: it HOLDs at `B`
and at `D` and fails at `A` and at `C`.

Reverse neighbor-read of cyclic lex-smallest frame transport at a cut holds if and only if neighbor-read
HOLDs at `A` and at `B` at that cut. Face neighbor-read of cyclic lex-smallest frame transport at a cut
holds if and only if neighbor-read HOLDs at `C` and at `D` at that cut. Either
side `UNDEFINED` is `UNDEFINED`. Else if both sides HOLD, reverse or face
HOLDs. Else fail.

Composition holds if and only if neighbor-read at `τ1` equals neighbor-read at
`τ2` at each of `A,B,C,D`. Either side `UNDEFINED` is `UNDEFINED`. Else if
the four neighbor-read bits agree across the two cuts, composition HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse and face without reading
cyclic signed columns; leftover-axis face fails while this face HOLDs.
Identifying split reverse with this reverse is refused: split HOLDs reverse
and face without the cyclic order of `Axis(M)`. Identifying leftover-empty
fail with this reverse is refused: leftover-empty fail scores empty leftover
as reverse fail and face fail, while this reverse HOLDs and this face HOLDs;
on unique signed `O={+e_1,+e_3}` leftover is empty while Orient is `+1`.
Identifying lexicographic unsigned `o1,o2` with this reverse is refused:
unsigned reverse fails and unsigned face HOLDs with `+1,+1`, while this
reverse HOLDs and this face HOLDs with `−1,−1` then `+1,+1`. Identifying
nm2orionex lex-one signed `e1<e2<e3` with this reverse is refused: lex-one
reverse fails from axis order independent of `m`, while this reverse HOLDs.
Identifying unique signed `|O_i|=1` with this reverse is refused: unique
signed reverse fails and face fails because each x-probe has an opposite
pair in `O`. Identifying leftover-axis orientation with this reverse is
refused: leftover-axis reverse HOLDs and face fails because C and D swap
`(m,pair)` columns, while this reverse HOLDs and this face HOLDs.
Identifying cyclic lex-largest with this reverse is refused: lex-largest
picks `−e` if both signs and reports opposite signs `−1,−1,+1,+1`.
Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, Orient, `F`, transport, and neighbor-read at `τ1` and `τ2`

On this process the four x-probes form. Compare to leftover axis: that
leftover reports empty leftover at each probe and leftover reverse fail
and leftover face fail. Compare to nm2ax cover and nm2ax12 split: both
HOLD reverse and face on this member. Compare to nm2oricycx cyclic
Orient: reverse HOLDs and face HOLDs from equal `±1` signs without a
sending matrix. Compare to scalar neighbor-read of Orient: HOLD at `A`,
`B`, and `D`, and fail at `C`. Compare to nm2chiralx lexicographic
unsigned `o1,o2` orientation: reverse fails and face HOLDs on this member
with signs `−1,+1,+1,+1`. Compare to nm2oridetx unique signed outgoing
letters: reverse fails and face fails because `|O_i|≠1`. Compare to
nm2orichx leftover-axis reverse HOLD whose face fails because C and D swap
`(m,pair)` columns. Compare to nm2orionex lex-one reverse fail whose face
HOLDs from `e1<e2<e3` order independent of `m`. This display reads the
neighbor-read of cyclic lex-smallest frame transport of `(m,o_next,o_prev)` of those same timed sets
at both cuts. Compare to nm2sfzfrm: that letter is the `t+1` cut alone, without
neighbor-read. Compare to nm2sfzrdx: that letter is neighbor-read at
`t+1` alone. Compare to nm2sfzfrmt2: that letter is transport freeze without
neighbor-read.

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ1) = {+e_3, −e_3}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_1}
M(D, τ1) = {+e_3, −e_3}
O(A, τ1) = {+e_1}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {−e_2, +e_3, −e_3}
O(D, τ1) = {+e_1, −e_1}
split(A, τ1) = fail
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = fail
m(A, τ1) = fail
i(A, τ1) = fail
o_next(A, τ1) fail
o_prev(A, τ1) fail
det(A, τ1) = fail
Orient(A, τ1) = fail
m(B, τ1) = +e_1
i(B, τ1) = 1
o_next(B, τ1) = +e_2
o_prev(B, τ1) = +e_3
det(B, τ1) = 1
Orient(B, τ1) = +1
m(C, τ1) = +e_1
i(C, τ1) = 1
o_next(C, τ1) = −e_2
o_prev(C, τ1) = +e_3
det(C, τ1) = -1
Orient(C, τ1) = −1
m(D, τ1) = fail
i(D, τ1) = fail
o_next(D, τ1) fail
o_prev(D, τ1) fail
det(D, τ1) = fail
Orient(D, τ1) = fail
F(A, τ1) = fail
F(B, τ1) = (+e_1, +e_2, +e_3)
F(C, τ1) = (+e_1, −e_2, +e_3)
F(D, τ1) = fail
transport(A, τ1) = fail
transport(B, τ1) = hold
transport(C, τ1) = hold
transport(D, τ1) = fail
neighbor-read(A, τ1) = fail
neighbor-read(B, τ1) = hold
neighbor-read(C, τ1) = hold
neighbor-read(D, τ1) = fail
scalar neighbor-read(A, τ1) = fail
scalar neighbor-read(B, τ1) = hold
scalar neighbor-read(C, τ1) = fail
scalar neighbor-read(D, τ1) = fail
witness(A, τ1) = fail
witness(B, τ1) = (0, 1, 1)
witness(C, τ1) = (2, 1, 0)
witness(D, τ1) = fail
read-witness(A, τ1) = fail
read-witness(B, τ1) = (0, 1, 1)
read-witness(C, τ1) = (2, 1, 0)
read-witness(D, τ1) = fail
M(A, τ2) = {+e_3, −e_3}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_1}
M(D, τ2) = {+e_3, −e_3}
O(A, τ2) = {+e_1}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {−e_2, +e_3, −e_3}
O(D, τ2) = {+e_1, −e_1}
Orient(A, τ2) = fail
Orient(B, τ2) = +1
Orient(C, τ2) = −1
Orient(D, τ2) = fail
F(A, τ2) = fail
F(B, τ2) = (+e_1, +e_2, +e_3)
F(C, τ2) = (+e_1, −e_2, +e_3)
F(D, τ2) = fail
transport(A, τ2) = fail
transport(B, τ2) = hold
transport(C, τ2) = hold
transport(D, τ2) = fail
neighbor-read(A, τ2) = fail
neighbor-read(B, τ2) = hold
neighbor-read(C, τ2) = hold
neighbor-read(D, τ2) = fail
scalar neighbor-read(A, τ2) = fail
scalar neighbor-read(B, τ2) = hold
scalar neighbor-read(C, τ2) = fail
scalar neighbor-read(D, τ2) = fail
witness(A, τ2) = fail
witness(B, τ2) = (0, 1, 1)
witness(C, τ2) = (2, 1, 0)
witness(D, τ2) = fail
read-witness(A, τ2) = fail
read-witness(B, τ2) = (0, 1, 1)
read-witness(C, τ2) = (2, 1, 0)
read-witness(D, τ2) = fail
```

`A` is not a seed: `t(A)=2` and `M(A)={+e_3,−e_3}`. Mixed remains a set:
`M(A,τ)` has two incoming steps and `O(B,τ)` has three outgoing steps.
Unique outgoing letters would assign `UNDEFINED` at mixed `O`. Unique
signed `|O_i|=1` fails at each probe: `O(A)` has both `±e_1`, `O(B)` has
both `±e_3`, `O(C)` has both `±e_1`, and `O(D)` has both `±e_3`.
Lex-smallest picks `+e` on each mixed cyclic slot, so `(o_next,o_prev)` is
defined. `M` is a singleton at each probe, so the unique signed `m`
exists. At each probe split HOLDs. Cover and split HOLD at each probe and
do not score that cyclic lex-smallest Orient is `+1,+1,−1,−1`. At `A`,
`i=2` so `e_next=e_3` and `e_prev=e_1`; mixed `O_prev={±e_1}` yields
`o_prev=+e_1`. At `B`, `i=1` so `e_next=e_2` and `e_prev=e_3`; mixed
`O_prev={±e_3}` yields `o_prev=+e_3`. Leftover-axis at `A` is pair `+e_1`
leftover `+e_3` and that Orient is `−1`; leftover-axis at `C` and `D` swap
`(m,pair)` columns and disagree. Lex-one at `B` uses axis order
`(+e_2,+e_3)` independent of `m` and reports `+1`, while cyclic
`(o_next,o_prev)=(+e_2,+e_3)` reports `+1`. Cyclic lex-largest at `A`
picks `o_prev=−e_1` and reports `−1`. O is not M.

On the 1-axis opposite two-site seed, `A=(0,0,1)` is a formed child at
tick 1 locking `+e_3`, and `C` is 2-in 1-out, so split fails at `C` and
Orient at `C` is fail, not UNDEFINED. That is leftover of the first pair.
Here both `(0,0,1)` and `(0,1,1)` are seeds of a second opposite pair on a
second axis. On the x-probes of this same seed, split HOLDs at `A` with
`m=−e_1` so `i=1`, `o_next=+e_2`, `o_prev=−e_3`, and cyclic Orient at that
x-probe is `+1`. X-probe `B` is `+1`, so x-probe reverse HOLDs as this
x-probe reverse HOLDs. X-probe `D` has split fail, so y-face fails.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,1)` is a
seed, so it is not a new 6-NN of `A`. The `t+2` neighbor of `A` forms with
earliest incoming `+e_3`, so `−e_2` does not enter `O(A,τ2)`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
new 6-NN of A at t(A)+2: none
new 6-NN of B at t(B)+2: none
new 6-NN of C at t(C)+2: none
new 6-NN of D at t(D)+2: none
```

`M` is frozen from `t` to `t+1` and from `t+1` to `t+2`. At `t`, `O` is
empty at each probe, split fails, Orient is fail, not UNDEFINED, and the
cyclic frame fails, not UNDEFINED. Transport at `t` therefore fails, not
UNDEFINED. Neighbor-read at `t` therefore fails, not UNDEFINED. Do not
score `τ=t`.

Each probe has a formed six-neighbor with split HOLD and a signed
permutation sending. Uniqueness of that neighbor is not required. First
witness in six-neighbor order: `A` sends to `D=(1,0,1)` with
`det(P)=-1=Orient(A)Orient(D)`; `B` sends to `(0,1,1)` with
`det(P)=-1`; `C` sends to `(0,1,2)` with `det(P)=-1`; `D` sends to
`A=(0,0,1)` with `det(P)=-1`. The first formed 6-NN in six-neighbor order
with transport HOLD is the same four sites. Neighbor-read HOLDs at each of
`A,B,C,D` at both cuts. Scalar neighbor-read HOLDs at `A`, `B`, and
`D`, and fails at `C`. Scalar reverse HOLDs as this reverse HOLDs. Scalar
face fails because `C` has no formed six-neighbor of equal Orient sign,
while neighbor-read face HOLDs. Unique nonnegative permutation sending HOLDs
at `B` and at `D` and fails at `A` and at `C`, so unique nonnegative
reverse fails and unique nonnegative face fails. The 3-split is a field:
opposite Orient at a neighbor is allowed when `det(P)` equals the product
of the two signs.

## Theorem 2 — reverse and face from neighbor-read of cyclic lex-smallest frame transport at `τ1` and `τ2`

Reverse neighbor-read of cyclic lex-smallest frame transport holds if and only if neighbor-read HOLDs at
`A` and at `B`. At `τ1`, `neighbor-read(A,τ1)=fail` and `neighbor-read(B,τ1)=hold`.
Reverse fails. At `τ2`, `neighbor-read(A,τ2)=fail` and `neighbor-read(B,τ2)=hold`.
Reverse fails. This is HOLD iff both neighbor-reads HOLD, not leftover of
nm2sfzfrm transport without a second-neighbor transport HOLD, not leftover of
nm2oricycx cyclic Orient equal signs, not leftover of scalar
neighbor-read, not leftover of equal transport bits including fail=fail,
not leftover of a unique nonnegative permutation sending,
not leftover of nm2chiralx lexicographic unsigned `o1,o2`, not leftover of
nm2oridetx unique signed outgoing letters, not leftover of nm2orichx
leftover-axis, not leftover of nm2orionex lex-one, not leftover of nm2ax
axis-cover, not leftover of nm2ax12 1-in 2-out split, not leftover-empty
fail, and not exist-opposite.

Reverse neighbor-read of cyclic lex-smallest frame transport at τ1: fail
Reverse neighbor-read of cyclic lex-smallest frame transport at τ2: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse fails
because cover fails at `A` and HOLDs at `B`. Split reverse fails because split
fails at `A` and HOLDs at `B`. Cover and split do not score handedness.
Leftover-axis reverse HOLDs with `−1,−1` bits, but leftover-axis
face fails because C and D swap `(m,pair)` columns while this face HOLDs.
Lexicographic unsigned reverse fails because unsigned `Orient(A)=−1` and
`Orient(B)=+1`. Unique signed reverse fails because both unique signed
signs fail. Lex-one signed reverse fails because lex-one `Orient(B)=+1`
from `e1<e2<e3` order independent of `m`. Cyclic lex-largest reverse
HOLDs with opposite signs `−1,−1`. Leftover-empty reverse fails because
leftover of the union is empty at `A` and at `B`. Leftover of `M` reverse
fails because leftover of `M` at `A` is `{e_1, e_3}` and at `B` is
`{e_2, e_3}`: nonempty and unequal. Leftover of `O` reverse fails because
leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`: nonempty and
unequal. Exist-opposite reverse of signed `M` fails. Exist-opposite
reverse of signed `O` holds. Presence of an opposite pair in `O` at `A`
and at `B` HOLDs. Those leftovers are not this display.

Reverse fails at both cuts.

Face neighbor-read of cyclic lex-smallest frame transport holds if and only if neighbor-read HOLDs at `C`
and at `D`. At `τ1`, `neighbor-read(C,τ1)=hold` and `neighbor-read(D,τ1)=fail`.
Face fails. At `τ2`, `neighbor-read(C,τ2)=hold` and `neighbor-read(D,τ2)=fail`.
Face fails.

Face neighbor-read of cyclic lex-smallest frame transport at τ1: fail
Face neighbor-read of cyclic lex-smallest frame transport at τ2: fail

Cover face fails because cover HOLDs at `C` and fails at `D`. Split face fails
because split HOLDs at `C` and fails at `D`. Cyclic lex-smallest oriented face
HOLDs because both signs are `−1`. Leftover-axis face fails because those
signs are `+1` and `−1`: C and D swap `(m,pair)` columns. Lex-one signed
oriented face HOLDs because both lex-one signs are `−1`; those signs are
these signs only as a leftover, not as this sending. Lexicographic unsigned face HOLDs because both unsigned
signs are `+1`; those unsigned columns are not cyclic `o_next,o_prev`.
Unique signed face fails because neither unique signed sign is `±1`.
Cover and split do not score handedness. Presence of an opposite pair in
`O` HOLDs at `C` and at `D`, so pair-presence face HOLDs while this face
also HOLDs from a different object: cyclic lex-smallest columns, not pair
presence. On the 1-axis opposite two-site seed, cover face HOLDs while
split face fails at `C` from 2-in 1-out, and Orient at `C` is fail, not
UNDEFINED. This three-axis far-face member is not leftover of that 1-axis split face
fail. The four x-probes of this same seed give cyclic Orient `+1` at `A`
and Orient fail at `D` from split fail, so oriented y-face fails while
this x-face HOLDs. The four x-probes give oriented reverse fail and
oriented face fail. Those probe-direction readouts are not this x-probe
display. Leftover-empty face fails because leftover of the union is empty
at `C` and at `D`. Leftover of `M` at `C` is `{e_1, e_2}` and leftover of
`M` at `D` is `{e_2, e_3}`: nonempty and unequal. Leftover of `O` at `C`
is `{e_3}` and leftover of `O` at `D` is `{e_1}`: nonempty and unequal.
Exist-opposite face of signed `M` fails. Exist-opposite face of signed
`O` fails. Cyclic lex-smallest oriented face HOLDs.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover HOLDs at `D` and split HOLDs at `D`. Orient at `D`
is `−1` from cyclic `(−e_2,+e_3)` even though `|O ∩ {±e_3}|=2`.

Face fails at both cuts.

## Theorem 3 — composition of neighbor-read of cyclic lex-smallest frame transport at `τ1` versus `τ2`

Composition HOLDs if and only if neighbor-read at `τ1` equals neighbor-read at
`τ2` at `A,B,C,D`. `neighbor-read(A,τ1)=neighbor-read(A,τ2)=fail`,
`neighbor-read(B,τ1)=neighbor-read(B,τ2)=hold`, `neighbor-read(C,τ1)=neighbor-read(C,τ2)=hold`,
`neighbor-read(D,τ1)=neighbor-read(D,τ2)=fail`. Composition HOLDs. fail=fail at `A` and at `D` is composition HOLD, not leftover of equal transport bits including fail=fail.

Composition of neighbor-read of cyclic lex-smallest frame transport: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

The reverse-and-face neighbor-read of nm2sfzrdx (reverse fail,
face fail at `t+1`) freezes at `t+2`: the four neighbor-read bits are
unchanged. That freeze is the present letter. It is not leftover of
nm2sfzrdx, which scores only one cut. It is not leftover of nm2sfzfrmt2,
which scores equality of transport rather than equality of neighbor-read.
On this member transport also freezes, so transport composition HOLDs as a
leftover; the scored object remains the four neighbor-read bits.
It is not leftover of nm2simt2x, which scores equality of `M` and of `O`.
On this member `M` and `O` also freeze, so simultaneous freeze HOLDs as a
leftover. Bit-stability of reverse HOLD and face HOLD is a leftover predicate:
those bits can agree while a probe neighbor-read flips, which composition of
neighbor-read would fail. Composition of neighbor-read at `τ=t` versus `τ=t+1`
fails because neighbor-read is fail at formation and hold at `t+1`. Do not
score `τ=t`.

## What this note does not claim

- It does not replace neighbor-read by neighbor-read of the scalar Orient sign.
- It does not replace neighbor-read by a unique nonnegative permutation sending.
- It does not replace neighbor-read by equal transport bits including fail=fail.
- It does not require a unique formed six-neighbor witness.
- It does not reprint nm2oricycx cyclic Orient reverse hold face hold as this neighbor-read.
- It does not reprint nm2sfzfrm cyclic lex-smallest frame transport at `t+1` alone.
- It does not reprint nm2sfzrdx neighbor-read at `t+1` alone.
- It does not reprint nm2sfzfrmt2 transport freeze without neighbor-read.
- It does not replace neighbor-read composition by nm2simt2x `M` and `O` freeze.
- It does not select a unique outgoing or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require outgoing sides to be singletons.
- It does not sum either set.
- It does not replace Orient by leftover-empty fail.
- It does not replace Orient by leftover of `M` alone.
- It does not replace Orient by leftover of `O` alone.
- It does not replace Orient by existential opposite of signed locks.
- It does not replace Orient by presence of an opposite pair in `O`.
- It does not replace Orient by lexicographic unsigned `o1,o2` orientation.
- It does not replace Orient by unique signed `|O_i|=1` letters.
- It does not replace Orient by leftover-axis orientation.
- It does not replace Orient by nm2orionex lex-one signed `e1<e2<e3`.
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
- It does not reprint nm2ax axis-cover reverse hold face hold as this
  oriented display.
- It does not reprint nm2ax12 1-in 2-out split reverse hold face hold as
  this oriented display.
- It does not reprint nm2chiralx lexicographic unsigned `o1,o2` reverse fail
  face hold with `+1,+1` as this oriented display.
- It does not reprint nm2oridetx unique signed reverse fail face fail as
  this oriented display.
- It does not reprint nm2orichx leftover-axis reverse hold face fail as
  this oriented display.
- It does not reprint nm2orionex lex-one reverse fail face hold as this
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
three-axis far-face opposite seed process, neighbor-read of cyclic lex-smallest frame transport of
`(m,o_next,o_prev)` of `M` and `O` at `t+1` versus `t+2`, reverse/face at
each cut, and composition of neighbor-read are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three-axis far-face opposite seed `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ1` and at `τ2` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ1` and at `τ2` | Theorem 1; HOLDING outgoing dual, freeze |
| split at both cuts | Theorem 1; fail, hold, hold, fail |
| unique signed `m`, axis index `i`, cyclic `(o_next,o_prev)` | Theorem 1; singleton `M`, lex-smallest pair defined |
| integer `det(m,o_next,o_prev)` at both cuts | Theorem 1; `1`, `1`, `-1`, `-1` at each cut |
| Orient at `τ1` | Theorem 1; fail, `+1`, `−1`, fail |
| Orient at `τ2` | Theorem 1; fail, `+1`, `−1`, fail |
| cyclic frame `F=(m,o_next,o_prev)` at both cuts | Theorem 1; LIVE three-axis at each probe |
| transport at `τ1` | Theorem 1; fail, hold, hold, fail |
| transport at `τ2` | Theorem 1; fail, hold, hold, fail |
| neighbor-read at `τ1` | Theorem 1; fail, hold, hold, fail |
| neighbor-read at `τ2` | Theorem 1; fail, hold, hold, fail |
| scalar neighbor-read of Orient | Theorem 1; fail, hold, fail, fail; scalar reverse fails, scalar face fails; not this letter |
| reverse from neighbor-read of cyclic-frame transport at `τ1` and at `τ2` | Theorem 2; `fail` at each cut |
| face from neighbor-read of cyclic-frame transport at `τ1` and at `τ2` | Theorem 2; `fail` at each cut |
| composition of neighbor-read of cyclic-frame transport | Theorem 3; `hold` |
| leftover of nm2sfzfrm `t+1` alone | not this freeze letter |
| leftover of nm2sfzrdx `t+1` alone | not this freeze letter |
| leftover of nm2sfzfrmt2 transport freeze | not this neighbor-read composition |
| leftover of nm2simt2x `M` and `O` freeze | not this neighbor-read composition |
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
| leftover of nm2chiralx lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2oridetx unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichx leftover-axis | not this oriented display |
| leftover of nm2orionex lex-one signed `e1<e2<e3` | not this oriented display |
| leftover of cyclic lex-largest | not this oriented display |
| leftover of nm2oricycx cyclic Orient equal signs | not this neighbor-read |
| leftover of scalar neighbor-read of Orient | not this neighbor-read |
| leftover of equal transport bits including fail=fail | not this neighbor-read |
| leftover of unique nonnegative permutation sending | not this neighbor-read |
| score at `τ=t` | refused |
| leftover of opposite-pair presence in `O` | not this oriented display |
| x-probe or x-probe Orient on this seed | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the 1-axis opposite two-site seed | not this display |
| leftover of the same-lock two-site seed | not this display; #7477 same-lock face transport fails |
| leftover of the LIVE three-axis three-site seed | not this display; face transport fails |
| split fail scored as `UNDEFINED` | refused; Orient fail |
| empty `O_i` scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: do the reverse-and-face neighbor-read bits of nm2sfzrdx freeze from `t+1` to `t+2` on the four x-probes of the three-axis far-face opposite seed. |
| V2 | Current main has no landed neighbor-read of cyclic-lex-smallest-frame-transport reverse/face composition of timed `M` and `O` at `t+1` versus `t+2` on these four x-probes of the three-axis far-face opposite seed. |
| V3 | Neighbor-read reports at two cuts, the reverse/face bits at each cut, and composition are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads a formed 6-NN that itself has transport HOLD at `B` and at `C` at each of `t+1` and `t+2`, reverse fails and face fails at both cuts while composition HOLDs, scalar neighbor-read fails at `C` while neighbor-read HOLDs at `C`, unique nonnegative reverse fails, nm2oricycx Orient equality does not supply the sending, nm2sfzrdx scores only one cut, and nm2sfzfrmt2 scores transport freeze without neighbor-read. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by nm2chiralx lexicographic unsigned `o1,o2`, does not replace
Orient by nm2oridetx unique signed `|O_i|=1`, does not replace Orient by
nm2orichx leftover-axis, does not replace Orient by nm2orionex lex-one,
does not replace Orient by cyclic lex-largest, does not replace Orient by
nmcover axis-cover, does not replace Orient by nm2ax axis-cover, does not
replace Orient by nm2ax12 1-in 2-out split, does not identify this
display with the 1-axis opposite two-site seed, does not identify it
with nmunopp union, does not replace this freeze by nm2sfzfrm `t+1`
alone, does not replace this freeze by nm2sfzrdx `t+1` alone, does not
replace this freeze by nm2sfzfrmt2 transport composition, and does not
replace neighbor-read composition by nm2simt2x `M` and
`O` freeze. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| scalar neighbor-read of Orient | reuse equal Orient sign at some formed 6-NN | scalar HOLDs at `A,B,D` and fails at `C`; scalar reverse HOLDs as this reverse HOLDs, but scalar face fails while this face HOLDs | ATTEMPTED |
| unique nonnegative permutation sending | require a unique sending with no minus signs | unique nonnegative sending HOLDs at `B,D` and fails at `A,C`; unique nonnegative reverse fails and unique nonnegative face fails while this reverse HOLDs and this face HOLDs; uniqueness is not required | ATTEMPTED |
| equal transport bits including fail=fail | score reverse/face as matching bits, including fail=fail | at `(0,-1,1)` transport fails and a formed 6-NN also fails, so equal-bit HOLDs while neighbor-read fails | ATTEMPTED |
| nm2sfzfrm `t+1` alone | reuse reverse hold and face hold at one cut | that letter has no `t+2` cut, no neighbor-read, and no composition | ATTEMPTED |
| nm2sfzrdx `t+1` alone | reuse neighbor-read reverse hold and face hold at one cut | that letter has no `t+2` cut and no neighbor-read composition | ATTEMPTED |
| nm2sfzfrmt2 transport freeze | score equality of transport bits | transport composition HOLDs here as leftover; composition of this letter is equality of neighbor-read bits | ATTEMPTED |
| nm2simt2x `M` and `O` freeze | score equality of lock sets | simultaneous freeze HOLDs here as leftover; composition of this letter is equality of neighbor-read bits | ATTEMPTED |
| reverse/face bit-stability | score reverse and face bits equal across cuts | those bits can agree while a probe neighbor-read flips; composition of neighbor-read would then fail | ATTEMPTED |
| nm2oricycx cyclic Orient | reuse Orient reverse hold and face hold from equal `±1` signs | Orient reverse HOLDs and face HOLDs without a signed-permutation sending; HOLDING cyclic #7451/#7452 is the frame sign, not transport | ATTEMPTED |
| nm2chiralx lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face hold | unsigned reverse fails while this reverse HOLDs; unsigned `o1,o2` at `C` is `(e_1,e_2)` while cyclic is `(−e_1,−e_2)` | ATTEMPTED |
| nm2oridetx unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed reverse fails and face fails while this reverse HOLDs and this face HOLDs; an opposite pair in `O` makes `|O_i|≠1` but lex-smallest still picks `+e` | ATTEMPTED |
| nm2orichx leftover-axis | reuse leftover-axis reverse hold and face fail | leftover-axis reverse HOLDs (`−1,−1`) as this reverse HOLDs, but leftover-axis face fails because C and D swap `(m,pair)` columns while this face HOLDs | ATTEMPTED |
| nm2orionex lex-one | reuse lex-one reverse fail and face hold | lex-one reverse fails from `e1<e2<e3` order independent of `m`; this reverse HOLDs from cyclic next/prev of `Axis(M)` | ATTEMPTED |
| cyclic lex-largest | reuse same cyclic axes with `−e` if both signs | lex-largest reverse HOLDs with `−1,−1` and face HOLDs with `+1,+1`; this Orient is `+1,+1,−1,−1` | ATTEMPTED |
| nm2ax axis-cover | reuse cover reverse hold and cover face hold on these x-probes | cover HOLDs reverse and face without cyclic signed columns; leftover-axis face fails while this face HOLDs | ATTEMPTED |
| nm2ax12 1-in 2-out split | reuse split reverse hold and split face hold | split HOLDs reverse and face without cyclic order of `Axis(M)`; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails while this reverse HOLDs; leftover face fails while this face HOLDs; unique signed `O={+e_1,+e_3}` has empty leftover and Orient `+1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal; leftover of `M` reverse fails while this reverse HOLDs | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`, nonempty unequal | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `O` holds as this reverse HOLDs; exist-opposite face of signed `O` fails while this face HOLDs | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence HOLDs at each of `A,B,C,D` without cyclic columns; leftover-axis face fails while this face HOLDs | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-smallest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is `+1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member both agree; flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient from `+1` to `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, Orient fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=2` and split fails at `A` | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails (`+1,−1`) and y-face fails; this letter is the four x-probes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the four x-probes | ATTEMPTED |
| score at `τ=t` | compose neighbor-read at formation versus `t+1` | leftover of nmot2opp; neighbor-read is fail at `t` and hold at `t+1`; Do not score `τ=t` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic-frame transport of own incoming and outgoing at `t+1` versus `t+2` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse hold and face hold on the three-axis far-face opposite seed | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is three disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `+e_3` while cyclic is `(+e_3,−e_1)` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of Orient with leftover of
`M` alone, missing identification of Orient with leftover-empty fail, missing
identification of Orient with existential opposite of signed locks, missing
identification of Orient with presence of an opposite pair in `O`, missing
identification of Orient with nm2chiralx lexicographic unsigned `o1,o2`,
missing identification of Orient with nm2oridetx unique signed `|O_i|=1`,
missing identification of Orient with nm2orichx leftover-axis, missing
identification of Orient with nm2orionex lex-one, missing identification of
Orient with cyclic lex-largest, missing identification of Orient with
nmcover axis-cover, missing identification of Orient with nm2ax axis-cover,
missing identification of Orient with nm2ax12 1-in 2-out split, missing
identification of this seed with the 1-axis opposite two-site seed, and
missing Record identification of Orient reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three disjoint opposite seed pairs `+e_1/−e_1`,
`+e_2/−e_2`, and `+e_3/−e_3`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ1=t+1`
and `τ2=t+2`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
next/prev axes of `Axis(M)`, lex-smallest signed outgoing letter under
`+e < −e` (hence `+e` if both signs), integer determinant sign, empty
`O_next` or empty `O_prev` as Orient fail not `UNDEFINED`, split fail as
Orient fail not `UNDEFINED`, four x-probes with formed, not seed, `A`, second pair as a
new seed not a formed child, third pair as a new seed not a formed child
on the `−z` face, mixed remains a set, and composition as
equality of neighbor-read at the two cuts are declared. No uniqueness of
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
| per element | neighbor-read of the cyclic lex-smallest frame transport HOLD bit at a formed 6-NN at a probe's `t+1` and `t+2` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports at `t+1` and `t+2`, reverse/face at each cut, composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for neighbor-read of cyclic-frame transport
reverse/face, a formation-rate rule, a later cut `t+3`, and a physical
selector among 1-in 2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Transport reverse hold and face hold are only leftover of
nm2oricycx cyclic Orient equal signs, or of neighbor-read of the scalar
Orient sign, or of cover and split; leftover-axis already answers reverse
HOLD; lex-one already answers face HOLD; unique signed `|O_i|=1` already
answers mixed `O`; leftover of `M` alone already answers reverse;
leftover of `O` alone already answers reverse; exist-opposite of signed
`O` already answers reverse; mixed #7188 already reported fail/fail; the
second pair is only the formed child `(0,0,1)` of the 1-axis seed; unique
outgoing letters should be required; cyclic lex-largest already gives
the same HOLD bits with opposite signs; unsigned incoming axis already
gives the same signs because each `M` letter is the positive unit;
because `M` and `O` freeze, composition is nm2simt2x; because reverse
HOLD and face HOLD at both cuts, composition is only bit-stability;
because transport also freezes, composition is nm2sfzfrmt2; and
nm2sfzrdx already answered reverse-and-face neighbor-read at `t+1`.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Neighbor-read reverse HOLDs because neighbor-read HOLDs at `A` and
at `B`. Neighbor-read face HOLDs because neighbor-read HOLDs at `C` and at `D`.
Scalar neighbor-read of Orient HOLDs at `A`, `B`, and `D` and fails at
`C`, so scalar reverse HOLDs and scalar face fails. HOLDING cyclic
#7451/#7452 Orient reverse HOLDs from equal signs without a sending
matrix; this reverse HOLDs from neighbor-read of a signed permutation of LIVE three-axis
frames. Unique nonnegative permutation sending HOLDs at `B,D` and fails at `A,C`.
Orient reverse HOLDs because `Orient(A)=+1` and
`Orient(B)=+1`. Orient face HOLDs because both signs are `−1`. Cover and
split HOLD reverse and face on this member and do not score cyclic signed
columns. Leftover-axis reverse HOLDs with `−1,−1` and face fails with
`+1,−1` because C and D swap `(m,pair)` columns; this reverse HOLDs and
this face HOLDs. Lex-one reverse fails from `e1<e2<e3` order independent of
`m`; this reverse HOLDs. Lexicographic unsigned `o1,o2` reverse fails with
`−1,+1` and face HOLDs with `+1,+1`. Unique signed `|O_i|=1` reverse fails
and face fails because each x-probe has an opposite pair in `O`; this face
HOLDs. Cyclic lex-largest reverse HOLDs with `−1,−1` and face HOLDs with
`+1,+1`; those signs are not these signs. Presence of an opposite pair in
`O` HOLDs at each of the four x-probes without cyclic columns. Leftover of
`M` alone at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`: nonempty unequal.
Leftover of `O` alone at `A` is `{e_2}` and at `B` is `{e_1}`. Unique
outgoing letters would assign `UNDEFINED` at mixed `O(A)`; this Orient is
`+1`, not `UNDEFINED`. On unique signed `O={+e_1,+e_3}` leftover is empty
while Orient is `+1`, so leftover-empty fail is not this predicate. Mixed
#7188 is a different z-symmetric process with mixed `M`. The second pair
is a new seed, not a formed child: `(0,0,1)` is recorded at tick 0 with
lock `+e_2`, whereas the 1-axis child forms at tick 1 with lock `+e_3`.
nm2sfzfrm scores only `τ=t+1`. nm2sfzrdx scores neighbor-read at `t+1`
alone. nm2sfzfrmt2 scores equality of transport. nm2simt2x scores equality of `M` and of
`O`. Reverse/face bit-stability can HOLD while a probe neighbor-read flips.
Reverse neighbor-read of cyclic lex-smallest frame transport is HOLD iff neighbor-read HOLDs at `A` and at
`B` at that cut, not leftover of leftover-axis and not leftover of
nm2orionex lex-one. Composition of neighbor-read of cyclic lex-smallest frame transport: hold.

### N8 — cross-cycle echo

nm2ax cover on this three-axis far-face seed reported cover HOLD at each of the four
x-probes, reverse hold, and face hold. nm2ax12 1-in 2-out split on the
same seed reported split HOLD at each of the four x-probes, reverse hold,
and face hold. nm2chiralx lexicographic unsigned `o1,o2` on the same seed
reported Orient `−1,+1,+1,+1`, reverse fail, and face hold. nm2oridetx
unique signed outgoing letters on the same seed reported Orient fail at
each probe, reverse fail, and face fail. nm2orichx leftover-axis on the
same seed reported Orient `−1,−1,+1,−1`, reverse hold, and face fail
because C and D swap `(m,pair)` columns. nm2orionex lex-one on the same
seed reported Orient `−1,+1,−1,−1`, reverse fail, and face hold from
`e1<e2<e3` order independent of `m`. Leftover axis reported empty leftover
at each of four x-probes, leftover reverse fail, and leftover face fail.
The four x-probes of this same seed reported cyclic Orient `+1` at `A`
from `m=−e_1` and Orient fail at `D` from split fail, so y-reverse HOLDs
and y-face fails. nm2oricycx cyclic next/prev lex-largest Orient on the
same seed reported HOLDING cyclic #7451/#7452 with Orient `−1,−1,+1,+1`,
reverse hold, and face hold from equal signs, without a sending matrix.
nm2sfzfrm cyclic lex-smallest frame transport on the same far-face seed reported transport HOLD
at each of `A,B,C,D`, reverse hold, and face hold at `t+1` alone. nm2sfzrdx
reported neighbor-read HOLD at each of `A,B,C,D`, reverse hold, and face
hold at `t+1` alone. nm2sfzfrmt2 reported transport freeze from `t+1` to
`t+2` without neighbor-read. nm2simt2x
reported simultaneous `M` and `O` freeze from `t+1` to `t+2`. This note is
not those displays: it reports neighbor-read of cyclic lex-smallest frame transport of
`(m,o_next,o_prev)` of `M` and `O` at `τ1=t+1` versus `τ2=t+2` on the
three-axis far-face opposite seed, with `t(A)=2`, `t(B)=1`, `t(C)=3`, and `t(D)=2`,
`neighbor-read=fail,hold,hold,fail` at `A,B,C,D` at both cuts, reverse fail at both
cuts, face fail at both cuts, and composition hold, while scalar
neighbor-read fails at `C` and unique nonnegative reverse fails. Cover and split do not score handedness.

**Gate disposition:** PASS for the neighbor-read of cyclic-lex-smallest-frame-transport `t+1` versus
`t+2` reverse/face reports and displayed composition above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the
unique singleton lock vector,” “the predicate equals six-neighbor lock
union,” “the predicate equals leftover-empty fail,” “the predicate equals
leftover of `M` alone,” “the predicate equals leftover of `O` alone,” “the
predicate equals exist-opposite HOLD,” “the predicate equals opposite-pair
presence in `O`,” “the predicate equals nm2chiralx lexicographic unsigned
`o1,o2` HOLD,” “the predicate equals nm2oridetx unique signed HOLD,” “the
predicate equals nm2orichx leftover-axis HOLD,” “the predicate equals
nm2orionex lex-one HOLD,” “the predicate equals cyclic lex-largest HOLD,”
“the predicate equals nm2oricycx cyclic Orient HOLD,” “the predicate
equals scalar neighbor-read of Orient HOLD,” “the predicate equals unique
nonnegative permutation sending HOLD,” “the predicate equals nmcover
axis-cover HOLD,” “the predicate equals nm2ax axis-cover HOLD,” “the
predicate equals nm2ax12 1-in 2-out split HOLD,” “the predicate equals
nm2sfzfrm `t+1` alone,” “the predicate equals nm2sfzrdx `t+1` alone,” “the predicate equals nm2sfzfrmt2 transport freeze,” “the predicate equals nm2simt2x `M` and `O`
freeze,” “the predicate equals equal transport bits including fail=fail,” “the predicate equals the 1-axis opposite two-site seed,” “the
predicate equals nmunopp union,” “bits are Admissibility,” “split fail is
UNDEFINED,” “empty `O_i` is UNDEFINED,” or “composition of neighbor-read of cyclic-frame
transport fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis far-face opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`
and `t+2`, reports the cyclic frame `F=(m,o_next,o_prev)`, reports Orient
as nm2oricyccx lex-smallest cyclic, reports transport by a
signed-permutation sending to some formed six-neighbor at each cut,
reports neighbor-read of that transport HOLD at a formed six-neighbor at
each cut, lists
new records in `B_3(0)` between `t` and `t+1` and between `t+1` and `t+2`
that meet a probe's six-neighbors, and checks Theorems 1--3. It also
checks that neighbor-read is fail, hold, hold, fail at `A,B,C,D` at both cuts while
scalar neighbor-read fails at `C`, that reverse fails and face fails
from neighbor-read at both cuts while scalar reverse fails and scalar face
fails, that composition HOLDs, that unique nonnegative permutation
sending HOLDs at `B,D` and fails at `A,C`, that HOLDING cyclic #7451/#7452 Orient
reverse HOLDs without being this sending, that leftover-axis face fails
because C and D swap `(m,pair)` columns and lex-one reverse fails from
`e1<e2<e3` order independent of `m`, that split fail is transport fail
not `UNDEFINED`, that empty `O_next` or empty `O_prev` is Orient fail not
`UNDEFINED`, that the 1-axis opposite two-site seed is a different member
with transport fail at `C`, that #7477 same-lock is a different member
with face transport fail, that LIVE three-axis as a three-site seed is a
different member with face transport fail, that leftover-empty fail is a
different predicate, that leftover of `M` alone and leftover of `O` alone
are different objects, that mixed sets remain sets, that the construction
does not sum, that a formation member from already-recorded six-neighbor
locks is not attached, that the second pair is a new seed not a formed
child, that the third pair is a new seed not a formed child, that the
y-probes and z-probes of this seed are not this letter,
that `τ=t` is not scored, and that the display is not the two-tick
lock-count clock composition. No runner cache is written.
