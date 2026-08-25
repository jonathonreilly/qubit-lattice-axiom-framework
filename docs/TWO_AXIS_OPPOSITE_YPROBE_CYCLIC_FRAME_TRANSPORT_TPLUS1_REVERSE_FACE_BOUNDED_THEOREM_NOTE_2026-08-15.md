---
claim_id: two_axis_opposite_yprobe_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic-frame transport of (m,o_next,o_prev) at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Cyclic-Frame Transport Of (m, o_next, o_prev) At t+1 Reverse And Face On Four Y-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** cyclic-frame transport of `(m,o_next,o_prev)` of simultaneous
earliest incoming set `M` and outgoing dual `O` at each probe's `τ=t+1`,
and reverse/face from that transport, on the four y-probes of the two-axis
opposite seed in `B_3(0)={n:n·n<=9}`. Same process and y-probes as nm2ax.
`M`, `O`, split as nm2ax12. Orient as nm2oricycy (lex-largest cyclic);
HOLDING cyclic #7451/#7452. Let `t(q)` be the formation tick of probe `q`.
Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming
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
Order `+e < −e`. `o_next` is the lex-largest vector in `O_next` (hence
`−e` if both signs). `o_prev` likewise. `Orient(q)` is the sign of the
integer determinant of the 3×3 matrix with columns `m`, `o_next`,
`o_prev`. If split fails, Orient fails, not `UNDEFINED`. When split
HOLDs, `F(q)=(m,o_next,o_prev)` is an oriented lattice frame: a LIVE
three-axis 1-in 2-out triple. Transport HOLDs at `q` if and only if split
HOLDs at `q`, `Orient(q)` is `±1`, and some formed six-neighbor `r` has
split HOLD, `Orient(r)` `±1`, and the 3×3 integer matrix sending the
columns of `F(q)` to the columns of `F(r)` is a signed permutation with
determinant `Orient(q)Orient(r)`. If split or Orient fails at `q`,
transport fails, not `UNDEFINED`. Reverse HOLDs if and only if transport
HOLDs at `A` and at `B`. Face HOLDs if and only if transport HOLDs at `C`
and at `D`. Neighbor-read of the scalar Orient sign fails site-locally at
`B` and at `D` on this member and HOLDs at `A` and at `C`, including #7477
same-lock as a different seed whose face transport fails, and including
LIVE three-axis as the frame itself rather than a scalar. Cover and split
do not score handedness. This is not leftover of nm2oricycy cyclic Orient
reverse fail from opposite `+1,−1` signs, not a signed-permutation sending.
This is not leftover of scalar neighbor-read of Orient. This is not
leftover of a unique nonnegative permutation sending. This is not leftover
of nm2orichy leftover-axis reverse fail whose `A` has no opposite pair in
`O`. This is not leftover of nm2orioney lex-one reverse HOLD from
`e1<e2<e3` order independent of `m`. This is not leftover of nm2chiraly
lexicographic unsigned `o1,o2` orientation. This is not leftover of unique
signed `|O_i|=1` unique signed outgoing letters. This is not leftover of
nm2ax axis-cover. This is not leftover of nm2ax12 1-in 2-out split. This is not leftover of leftover-of-`M` alone. This is
not leftover of leftover-of-`O` alone. This is not leftover-empty fail of
leftover axis. This is not leftover of nmunopp union. This is not leftover
of nmt2opp `M` frozen at `t`. This is not leftover of nmot2opp two-tick
composition. This is not leftover of nmoutopp untimed eventual-`O`. This
is not leftover of mixed #7188 fail/fail. This is not leftover of the
1-axis opposite two-site seed. This is not leftover of the same-lock
two-site seed. The second pair is a new seed, not a formed child.
Uniqueness is not required. Mixed remains a set. Displayed, not adopted.
Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

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
`Axis(M)` under `+e < −e`. When split HOLDs, `F=(m,o_next,o_prev)` is
that LIVE three-axis frame. Transport is existential: some formed
six-neighbor hosts a split-HOLDING frame whose columns are a signed
permutation of the source columns with determinant the product of the
two Orient signs. Reverse and face are scored on transport HOLD at the
paired probes. Neighbor-read of the scalar Orient sign is a different
readout and is not used as the object. A unique nonnegative permutation
sending is a different readout and is not used as the object. Named
signs `{+,−}` of locks are a coarser readout and are not used as the
object. A singleton unique outgoing lock letter is a different readout
and is not used as the object. Unsigned axis units of `Axis(O)` are a
different readout and are not used. Unique signed letters requiring
`|O_i|=1` are a different readout and are not used. Opposite-pair
leftover-axis orientation is a different readout and is not used.
Lex-one signed outgoing letters in axis order `e1<e2<e3` independent of
`m` are a different readout and are not used. Cyclic lex-smallest (`+e`
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
claim_type_reason: "Exact report of cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 on the four y-probes of the two-axis opposite seed, transport at A,B,C hold and D fail, reverse hold and face fail from transport at paired probes; uniqueness of the sending neighbor is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_yprobe_cyclic_frame_transport_tplus1_reverse_face
target_blocker_text: "display cyclic-frame transport of (m,o_next,o_prev) reverse/face on the four y-probes of the two-axis opposite seed, not scalar neighbor-read of Orient, not unique nonnegative sending, not leftover-axis, not lex-one e1<e2<e3, not unique |O_i|=1, not unsigned axis units, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 displayed; do not write transport into Admissibility, do not reduce to scalar neighbor-read of Orient, do not reduce to unique nonnegative permutation sending, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-smallest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace transport by unique outgoing letters, do not replace transport by existential opposite of signed locks, do not replace transport by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 on the four y-probes of the two-axis opposite seed and reverse/face from that transport; displayed, not adopted"
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
cyclic-frame transport of `F=(m,o_next,o_prev)` of `M` and `O` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the first opposite pair. Same process and
y-probes as nm2ax.

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

## Named cyclic-frame transport of `(m,o_next,o_prev)` at `τ=t+1`

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
```

Neighbor-read of the scalar Orient sign HOLDs at `q` if and only if
`Orient(q)` is `±1` and some formed six-neighbor has the same sign. That
is a different object: it fails at `B` and at `D` on this member while
transport HOLDs at `B`, because a signed permutation may send a frame to a
neighbor of opposite Orient with `det(P)=Orient(q)Orient(r)`. A unique
nonnegative permutation sending is a different object: it HOLDs at `C` and
fails at `A`, `B`, and `D`. Uniqueness is not required.

Reverse cyclic-frame transport holds if and only if transport HOLDs at
`A` and at `B`. Face cyclic-frame transport holds if and only if
transport HOLDs at `C` and at `D`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides HOLD, reverse or face HOLDs. Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse and fails face without reading
cyclic signed columns; Orient reverse fails while this reverse HOLDs.
Identifying split reverse with this reverse is refused: split HOLDs reverse
and fails face without the cyclic order of `Axis(M)`. Identifying leftover-empty
fail with this reverse is refused: leftover-empty fail scores empty leftover
as reverse fail and face fail, while this reverse HOLDs; leftover of the
union at `A` is empty while `Orient(A)=+1`. Identifying lexicographic
unsigned `o1,o2` with this reverse is refused: unsigned reverse fails with
`−1,+1` while this reverse HOLDs. Identifying nm2orioney lex-one signed
`e1<e2<e3` with this reverse is refused: lex-one reverse HOLDs from axis
order independent of `m`; those signs are not this sending. Identifying
unique signed `|O_i|=1` with this reverse is refused: unique signed reverse
fails because `B` is mixed. Identifying leftover-axis orientation with this
reverse is refused: leftover-axis reverse fails because `A` has no opposite
pair in `O`, while this reverse HOLDs. Identifying cyclic lex-smallest with
this reverse is refused: lex-smallest reverse HOLDs with `+1,+1` while
cyclic lex-largest reverse fails from `+1,−1`. Identifying a named sign of
those locks with reverse or face is refused: named-sign lettering lost the
axis.

## Theorem 1 — ticks, `M`, `O`, split, Orient, `F`, and transport at `τ=t+1`

On this process the four y-probes form. Compare to leftover axis: leftover
of the union is empty at `A`, `B`, and `C` and is `{e_2}` at `D`, leftover
reverse fail and leftover face fail. Compare to nm2ax cover and nm2ax12
split: both HOLD reverse and fail face on this member. Compare to
nm2oricycy cyclic Orient: reverse fails from opposite `+1,−1` signs and
face fails from Orient fail at `D`, without a sending matrix. Compare to
scalar neighbor-read of Orient: HOLD at `A` and at `C`, fail at `B` and at
`D`. Compare to nm2chiraly lexicographic unsigned `o1,o2` orientation:
reverse fails and face fails on this member with signs `−1,+1,−1`, fail.
Compare to unique signed `|O_i|=1` unique signed outgoing letters: reverse
fails and face fails; unique signed HOLDs at `A` and fails at mixed `O` of
`B`, `C`, and `D`. Compare to nm2orichy leftover-axis reverse fail because
`A` has no opposite pair in `O`. Compare to nm2orioney lex-one reverse HOLD
from `e1<e2<e3` order independent of `m`. This display reads the
cyclic-frame transport of `(m,o_next,o_prev)` of those same timed sets:

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
o_prev(B) = −e_3
det(B) = -1
Orient(B) = −1
m(C) = +e_2
i(C) = 2
o_next(C) = −e_3
o_prev(C) = −e_1
det(C) = 1
Orient(C) = +1
Orient(D) = fail
F(A) = (−e_1, +e_2, −e_3)
F(B) = (+e_1, +e_2, −e_3)
F(C) = (+e_2, −e_3, −e_1)
F(D) = fail
transport(A) = hold
transport(B) = hold
transport(C) = hold
transport(D) = fail
scalar neighbor-read(A) = hold
scalar neighbor-read(B) = fail
scalar neighbor-read(C) = hold
scalar neighbor-read(D) = fail
witness(A) = (0, 2, 0)
P(A→witness) = [0 0 1; 1 0 0; 0 1 0]
det P(A) = 1
witness(B) = (0, 1, 1)
P(B→witness) = [0 0 -1; -1 0 0; 0 -1 0]
det P(B) = -1
witness(C) = (0, 1, 0)
P(C→witness) = [0 1 0; 0 0 1; 1 0 0]
det P(C) = 1
witness(D) = fail
```

`A` is a seed at tick 0 with seed letter `−e_1`. Mixed remains a set:
`O(A,τ)` has two outgoing steps, `O(B,τ)` has three, `O(C,τ)` has four,
and `O(D,τ)` has two. Unique outgoing letters would assign `UNDEFINED` at
mixed `O`. Unique signed `|O_i|=1` HOLDs at `A` and fails at `B`, `C`, and
`D`: `O(B)` has both `±e_3`, `O(C)` has both `±e_1` and both `±e_3`, and
`O(D)` has both `±e_1`. Lex-largest picks `−e` on each mixed cyclic slot,
so `(o_next,o_prev)` is defined at `A`, `B`, and `C`. `M` is a singleton
at each probe, so the unique signed `m` exists. Split HOLDs at `A`, `B`,
and `C` and fails at `D`. Cover HOLDs at `A`, `B`, and `C` and fails at
`D` because `Axis(M)={e_3}` and `Axis(O)={e_1}` miss `e_2`. Cover and
split HOLD reverse and fail face and do not score that cyclic lex-largest
Orient is `+1,−1,+1`, fail. At `A`, `i=1` so `e_next=e_2` and
`e_prev=e_3`; `O_next={+e_2}` and `O_prev={−e_3}`. At `B`, `i=1` so
`e_next=e_2` and `e_prev=e_3`; mixed `O_prev={±e_3}` yields
`o_prev=−e_3`. At `C`, `i=2` so `e_next=e_3` and `e_prev=e_1`; mixed
slots yield `o_next=−e_3` and `o_prev=−e_1`. Leftover-axis at `A` fails
because `O(A)` has no opposite pair. Lexicographic unsigned at `A` uses
`(e_2,e_3)` and reports `−1`, while cyclic `(+e_2,−e_3)` reports `+1`.
Unsigned incoming axis at `A` replaces `m=−e_1` by `+e_1` and reports
`−1`. Cyclic lex-smallest at `B` picks `o_prev=+e_3` and reports `+1`.
O is not M.

On the 1-axis opposite two-site seed, `A=(0,1,0)` is still a seed at tick
0 locking `−e_1`, `t(B)=2`, `t(D)=3`, cover HOLDs at `D` from 2-in 1-out,
and transport face fails at `D`. That is leftover of the first pair. Here
both `(0,0,1)` and `(0,1,1)` are seeds of a second opposite pair on a
second axis, `t(B)=1`, and `t(D)=2`. On the z-probes of this same seed,
transport HOLDs at each of `A,B,C,D`, reverse HOLDs, and face HOLDs, while
this y-probe reverse HOLDs and this y-face fails. Z-probe Orient reverse
HOLDs from equal `−1,−1` while this Orient reverse fails from `+1,−1`.
X-probe reverse fails and x-face fails.

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
`C`, while `O(D,t)={−e_1}` is nonempty. Split fails at `t` at each probe,
Orient is fail, not UNDEFINED, and the cyclic frame fails, not UNDEFINED.
Transport at `t` therefore fails, not UNDEFINED.

`A`, `B`, and `C` each have a formed six-neighbor with split HOLD and a
signed permutation sending. `D` has split fail, so transport fails, not
UNDEFINED. Uniqueness of that neighbor is not required. First witness in
six-neighbor order: `A` sends to `C=(0,2,0)` with
`det(P)=1=Orient(A)Orient(C)`; `B` sends to `(0,1,1)` with `det(P)=-1`;
`C` sends to `A=(0,1,0)` with `det(P)=1`; `D` has no witness. Scalar
neighbor-read HOLDs at `A` and at `C` and fails at `B` and at `D`, so
scalar reverse fails and scalar face fails while transport reverse HOLDs
and transport face fails. Unique nonnegative permutation sending HOLDs at
`C` (the sending to `A` has no minus signs) and fails at `A`, `B`, and
`D`; uniqueness is not required. The 3-split is a field: opposite Orient
at a neighbor is allowed when `det(P)` equals the product of the two
signs. `B` transports to a neighbor of opposite Orient.

## Theorem 2 — reverse from cyclic-frame transport at `τ`

Reverse cyclic-frame transport holds if and only if transport HOLDs at
`A` and at `B`. `transport(A)=hold` and `transport(B)=hold`. Reverse
HOLDs. This is HOLD iff both transports HOLD, not leftover of nm2oricycy
cyclic Orient equal signs, not leftover of scalar neighbor-read, not
leftover of a unique nonnegative permutation sending, not leftover of
nm2chiraly lexicographic unsigned `o1,o2`, not leftover of unique signed
`|O_i|=1` unique signed outgoing letters, not leftover of nm2orichy
leftover-axis, not leftover of nm2orioney lex-one, not leftover of nm2ax
axis-cover, not leftover of nm2ax12 1-in 2-out split, not leftover-empty
fail, and not exist-opposite.

Reverse cyclic-frame transport at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness: Orient
at `A` is `+1` and at `B` is `−1`. Cyclic Orient reverse fails from those
opposite signs while this reverse HOLDs from signed-permutation sendings.
Leftover-axis reverse fails because leftover-axis at `A` is fail from no
opposite pair in `O`. Lexicographic unsigned reverse fails because
unsigned `Orient(A)=−1` and `Orient(B)=+1`. Unique signed reverse fails
because unique signed at `B` fails from mixed `±e_3`. Lex-one signed
reverse HOLDs with `+1,+1` from `e1<e2<e3` order independent of `m`; those
signs are not these transport bits. Cyclic lex-smallest reverse HOLDs with
`+1,+1` while cyclic lex-largest reverse fails. Leftover-empty reverse
fails because leftover of the union is empty at `A` and at `B`. Leftover
of `M` reverse HOLDs because leftover of `M` at `A` and at `B` is
`{e_2, e_3}`: nonempty and equal; leftover of `M` is unsigned leftover of
`Axis(M)`, not a sending. Leftover of `O` reverse HOLDs because leftover
of `O` at `A` and at `B` is `{e_1}`: nonempty and equal. Exist-opposite
reverse of signed `M` holds. Exist-opposite reverse of signed `O` holds.
Presence of an opposite pair in `O` fails at `A` and HOLDs at `B`, so
pair-presence reverse fails. Those leftovers are not this display.

Reverse HOLDs.

## Theorem 3 — face from cyclic-frame transport at `τ`

Face cyclic-frame transport holds if and only if transport HOLDs at `C`
and at `D`. `transport(C)=hold` and `transport(D)=fail`. Face fails.

Face cyclic-frame transport at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover HOLDs at `C` and fails at `D`. Split face
fails because split HOLDs at `C` and fails at `D`. Cyclic lex-largest
oriented face fails because Orient at `D` is fail, not UNDEFINED. Cover
and split do not score handedness. Presence of an opposite pair in `O`
HOLDs at `C` and at `D`, so pair-presence face HOLDs while this face
fails. Exist-opposite face of signed `O` HOLDs because both sides contain
`±e_1`, while this face fails. Unique nonnegative sending HOLDs at `C` and
fails at `D`, so unique nonnegative face fails. On the 1-axis opposite
two-site seed, cover face HOLDs while split face fails at `D` from 2-in
1-out, and transport face fails at `D`. This two-axis member has cover
face fail because `D` misses `e_2`, which the 1-axis cover face does not.
The four z-probes of this same seed give transport HOLD at each probe,
reverse hold, and face hold, while this y-face fails. The four x-probes
give oriented reverse fail and oriented face fail. Those probe-direction
readouts are not this y-probe display. Leftover-empty face fails because
leftover of the union is empty at `C` and is `{e_2}` at `D`. Leftover of
`M` at `C` is `{e_1, e_3}` and leftover of `M` at `D` is `{e_1, e_2}`:
nonempty and unequal. Leftover of `O` at `C` is `{e_2}` and leftover of
`O` at `D` is `{e_2, e_3}`: nonempty and unequal. Exist-opposite face of
signed `M` fails. Cyclic lex-largest oriented face fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover fails at `D` and split fails at `D`. Orient at
`D` is fail, not UNDEFINED, from split fail, even though `M(D)` is the
singleton `−e_3`.

Face fails.

## What this note does not claim

- It does not replace transport by neighbor-read of the scalar Orient sign.
- It does not replace transport by a unique nonnegative permutation sending.
- It does not require a unique formed six-neighbor witness.
- It does not reprint nm2oricycy cyclic Orient reverse fail face fail as this transport.
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
- It does not replace Orient by nm2orioney lex-one signed `e1<e2<e3`.
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
- It does not reprint nm2chiraly lexicographic unsigned `o1,o2` reverse fail
  face hold with `+1,+1` as this oriented display.
- It does not reprint unique signed |O_i|=1 unique signed reverse fail face fail as
  this oriented display.
- It does not reprint nm2orichy leftover-axis reverse fail face fail as
  this oriented display.
- It does not reprint nm2orioney lex-one reverse hold face fail as this
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
two-axis opposite seed process, cyclic-frame transport of
`(m,o_next,o_prev)` of `M` and `O` at `t+1`, and the reverse/face bits
from that transport are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual; `O(D,t)` already nonempty |
| split at `τ` | Theorem 1; HOLD at `A,B,C`; fail at `D` |
| unique signed `m`, axis index `i`, cyclic `(o_next,o_prev)` | Theorem 1; singleton `M`; pair defined at `A,B,C`; fail at `D` |
| integer `det(m,o_next,o_prev)` | Theorem 1; `1`, `-1`, `1`, fail |
| Orient at `τ` | Theorem 1; `+1`, `−1`, `+1`, fail |
| cyclic frame `F=(m,o_next,o_prev)` | Theorem 1; LIVE three-axis at `A,B,C`; fail at `D` |
| transport at `τ` | Theorem 1; HOLD at `A,B,C`; fail at `D` |
| scalar neighbor-read of Orient | Theorem 1; HOLD at `A,C`, fail at `B,D`; not this letter |
| reverse from cyclic-frame transport at `τ` | Theorem 2; `hold` |
| face from cyclic-frame transport at `τ` | Theorem 3; `fail` |
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
| leftover of nm2chiraly lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of unique signed |O_i|=1 unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichy leftover-axis | not this oriented display |
| leftover of nm2orioney lex-one signed `e1<e2<e3` | not this oriented display |
| leftover of cyclic lex-smallest | not this oriented display |
| leftover of nm2oricycy cyclic Orient opposite signs | not this transport |
| leftover of scalar neighbor-read of Orient | not this transport |
| leftover of unique nonnegative permutation sending | not this transport |
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
| V1 | It answers the first-display question: cyclic-frame transport of `(m,o_next,o_prev)` of `M` and `O` at `t+1` on the four y-probes of the two-axis opposite seed, and reverse/face from that transport. |
| V2 | Current main has no landed cyclic-frame-transport reverse/face of timed `M` and `O` on these four y-probes of the two-axis opposite seed. |
| V3 | Transport reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads a signed-permutation sending of the cyclic frame to a formed six-neighbor at the same `t+1` cut, reverse HOLDs while nm2oricycy Orient reverse fails from opposite `+1,−1` signs, face fails at split-fail `D`, scalar neighbor-read reverse fails, and unique nonnegative sending HOLDs only at `C`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by nm2chiraly lexicographic unsigned `o1,o2`, does not replace
Orient by unique signed |O_i|=1 unique signed `|O_i|=1`, does not replace Orient by
nm2orichy leftover-axis, does not replace Orient by nm2orioney lex-one,
does not replace Orient by cyclic lex-smallest, does not replace Orient by
nmcover axis-cover, does not replace Orient by nm2ax axis-cover, does not
replace Orient by nm2ax12 1-in 2-out split, does not identify this
display with the 1-axis opposite two-site seed, and does not identify it
with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| scalar neighbor-read of Orient | reuse equal Orient sign at some formed 6-NN | scalar HOLDs at `A,C` and fails at `B,D`; scalar reverse fails while this reverse HOLDs | ATTEMPTED |
| unique nonnegative permutation sending | require a unique sending with no minus signs | unique nonnegative sending HOLDs at `C` and fails at `A,B,D`; uniqueness is not required | ATTEMPTED |
| nm2oricycy cyclic Orient | reuse Orient reverse fail and face fail from opposite `±1` signs | Orient reverse fails from `+1,−1` without a signed-permutation sending; this reverse HOLDs from sendings | ATTEMPTED |
| nm2chiraly lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face fail | unsigned reverse fails as this reverse HOLDs; unsigned `o1,o2` at `A` is `(e_2,e_3)` while cyclic is `(+e_2,−e_3)` | ATTEMPTED |
| unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed HOLDs at `A` and fails at mixed `B,C,D`; reverse fails while this reverse HOLDs | ATTEMPTED |
| nm2orichy leftover-axis | reuse leftover-axis reverse fail and face fail | leftover-axis reverse fails because `A` has no opposite pair in `O` while this reverse HOLDs | ATTEMPTED |
| nm2orioney lex-one | reuse lex-one reverse hold and face fail | lex-one reverse HOLDs from `e1<e2<e3` order independent of `m`; those signs are not this sending | ATTEMPTED |
| cyclic lex-smallest | reuse same cyclic axes with `+e` if both signs | lex-smallest reverse HOLDs with `+1,+1` while cyclic lex-largest reverse fails from `+1,−1` | ATTEMPTED |
| nm2ax axis-cover | reuse cover reverse hold and cover face fail on these y-probes | cover HOLDs reverse and fails face without cyclic signed columns; Orient reverse fails while this reverse HOLDs | ATTEMPTED |
| nm2ax12 1-in 2-out split | reuse split reverse hold and split face fail | split HOLDs reverse and fails face without cyclic order of `Axis(M)`; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails while this reverse HOLDs; leftover of the union at `A` is empty while `Orient(A)=+1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and at `B` is `{e_2,e_3}`, nonempty equal so leftover-of-`M` reverse HOLDs; leftover of `M` is unsigned leftover, not a sending | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and at `B` is `{e_1}`, nonempty equal; leftover of `O` is unsigned leftover, not a sending | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `O` holds as this reverse HOLDs; exist-opposite face of signed `O` HOLDs while this face fails | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence fails at `A` and HOLDs at `B,C,D`; pair-presence reverse fails while this reverse HOLDs; pair-presence face HOLDs while this face fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-largest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set of two letters; unique-letter Orient is `UNDEFINED` while this Orient is `+1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | at `A`, unsigned incoming reports `−1` while cyclic Orient is `+1` because `m=−e_1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `D` is cover fail, not 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(B)=2`, `t(D)=3`, mixed `M(D)`, cover face HOLD | different seed; second pair is a new seed, not a formed child; here `t(B)=1`, `t(D)=2`, and cover fails at `D` | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe reverse HOLDs and z-face HOLDs; this letter is the four y-probes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the four y-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-largest outgoing determinant orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse hold and face fail on the two-axis opposite seed | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is two disjoint opposite pairs; `M(A)={−e_1}` not `{+e_1}` | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `(0,1,−1)` while cyclic is `(+e_2,−e_3)` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of Orient with leftover of
`M` alone, missing identification of Orient with leftover-empty fail, missing
identification of Orient with existential opposite of signed locks, missing
identification of Orient with presence of an opposite pair in `O`, missing
identification of Orient with nm2chiraly lexicographic unsigned `o1,o2`,
missing identification of Orient with unique signed |O_i|=1 unique signed `|O_i|=1`,
missing identification of Orient with nm2orichy leftover-axis, missing
identification of Orient with nm2orioney lex-one, missing identification of
Orient with cyclic lex-smallest, missing identification of Orient with
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
next/prev axes of `Axis(M)`, lex-largest signed outgoing letter under
`+e < −e` (hence `−e` if both signs), integer determinant sign, empty
`O_next` or empty `O_prev` as Orient fail not `UNDEFINED`, split fail as
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
| per element | cyclic frame `F=(m,o_next,o_prev)` and signed-permutation sending to a formed 6-NN | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four transport reports, reverse/face from transport at paired probes | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for cyclic-frame transport
reverse/face, a formation-rate rule, and a physical selector among 1-in
2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Transport reverse hold and face fail are only leftover of
nm2oricycy cyclic Orient opposite signs, or of neighbor-read of the
scalar Orient sign, or of cover and split; leftover of `M` alone already
answers reverse HOLD; leftover of `O` alone already answers reverse HOLD;
exist-opposite of signed `O` already answers reverse HOLD and face HOLD;
lex-one already answers reverse HOLD; cyclic lex-smallest already gives
the same reverse HOLD bits with `+1,+1`; unique nonnegative sending
already HOLDs at `C`; mixed #7188 already reported fail/fail; the second
pair is only the formed child of the 1-axis seed; unique outgoing letters
should be required; and unsigned incoming axis already gives the same
signs because each `M` letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Transport reverse HOLDs because transport HOLDs at `A` and
at `B`. Transport face fails because transport fails at `D` from split
fail. Scalar neighbor-read of Orient HOLDs at `A` and at `C` and fails at
`B` and at `D`, so scalar reverse fails while this reverse HOLDs.
nm2oricycy Orient reverse fails from opposite `+1,−1` signs without a
sending matrix; this reverse HOLDs from a signed permutation of LIVE
three-axis frames. Unique nonnegative permutation sending HOLDs at `C`
and fails at `A`, `B`, and `D`; uniqueness is not required. Orient reverse
fails because `Orient(A)=+1` and `Orient(B)=−1`. Cover and split HOLD
reverse and fail face on this member and do not score cyclic signed
columns. Leftover-axis reverse fails because `A` has no opposite pair in
`O`. Lex-one reverse HOLDs from `e1<e2<e3` order independent of `m`; those
signs are not this sending. Lexicographic unsigned `o1,o2` reverse fails
with `−1,+1`. Unique signed `|O_i|=1` reverse fails because `B` is mixed.
Cyclic lex-smallest reverse HOLDs with `+1,+1` while cyclic lex-largest
reverse fails. Presence of an opposite pair in `O` fails at `A`. Leftover
of `M` alone at `A` and at `B` is `{e_2,e_3}`: nonempty equal, so
leftover-of-`M` reverse HOLDs as unsigned leftover, not a sending.
Leftover of `O` alone at `A` and at `B` is `{e_1}`. Unique outgoing
letters would assign `UNDEFINED` at mixed `O(A)`; this Orient is `+1`, not
`UNDEFINED`. Unsigned incoming at `A` reports `−1` while cyclic Orient is
`+1` because `m=−e_1`. Exist-opposite face of signed `O` HOLDs while this
face fails. Mixed #7188 is a different z-symmetric process with mixed
`M`. The second pair is a new seed, not a formed child: `(0,0,1)` is
recorded at tick 0 with lock `+e_2`. Reverse transport is HOLD iff
transport HOLDs at `A` and at `B`, not leftover of cyclic Orient equal
signs.

### N8 — cross-cycle echo

nm2ax cover on this two-axis seed reported cover HOLD at `A,B,C`, cover
fail at `D`, reverse hold, and face fail. nm2ax12 1-in 2-out split on the
same seed reported split HOLD at `A,B,C`, split fail at `D`, reverse hold,
and face fail. nm2chiraly lexicographic unsigned `o1,o2` on the same seed
reported Orient `−1,+1,−1`, fail, reverse fail, and face fail. Unique
signed `|O_i|=1` outgoing letters on the same seed reported Orient `+1` at
`A` and fail at mixed `B,C,D`, reverse fail, and face fail. nm2orichy
leftover-axis on the same seed reported leftover-axis fail at `A` from no
opposite pair. nm2orioney lex-one on the same seed reported reverse HOLD
from `e1<e2<e3` order independent of `m`. Leftover axis reported empty
leftover at `A,B,C` and leftover `{e_2}` at `D`, leftover reverse fail,
and leftover face fail. The four z-probes of this same seed reported
transport HOLD at each probe, reverse hold, and face hold. nm2oricycy
cyclic next/prev lex-largest Orient on the same seed reported Orient
`+1,−1,+1`, fail, reverse fail from opposite signs, and face fail, without
a sending matrix. This note is not those displays: it reports cyclic-frame
transport of `(m,o_next,o_prev)` of `M` and `O` at `τ=t+1` on the
two-axis opposite seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`, and `t(D)=2`,
`transport(A)=hold`, `transport(B)=hold`, `transport(C)=hold`,
`transport(D)=fail`, reverse hold, and face fail, while scalar
neighbor-read fails at `B,D` and cyclic Orient reverse fails. Cover and
split do not score handedness.

**Gate disposition:** PASS for the cyclic-frame-transport `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals nm2chiraly lexicographic unsigned `o1,o2`
HOLD,” “the predicate equals unique signed |O_i|=1 unique signed HOLD,” “the
predicate equals nm2orichy leftover-axis HOLD,” “the predicate equals
nm2orioney lex-one HOLD,” “the predicate equals cyclic lex-smallest HOLD,”
“the predicate equals nm2oricycy cyclic Orient HOLD,” “the predicate
equals scalar neighbor-read of Orient HOLD,” “the predicate equals unique
nonnegative permutation sending HOLD,” “the predicate equals nmcover
axis-cover HOLD,” “the predicate equals nm2ax axis-cover HOLD,” “the
predicate equals nm2ax12 1-in 2-out split HOLD,” “the predicate equals
the 1-axis opposite two-site seed,” “the predicate equals nmunopp union,”
“bits are Admissibility,” “split fail is UNDEFINED,” or “empty `O_i` is
UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports split of the pair, reports the cyclic frame
`F=(m,o_next,o_prev)`, reports Orient as nm2oricycy lex-largest cyclic,
reports transport by a signed-permutation sending to some formed
six-neighbor, lists new records in `B_3(0)` between `t` and `t+1` that
meet a probe's six-neighbors, and checks Theorems 1--3. It also checks
that transport HOLDs at `A,B,C` and fails at `D` while scalar neighbor-read
fails at `B,D`, that reverse HOLDs and face fails from transport while
scalar reverse fails and cyclic Orient reverse fails, that unique
nonnegative permutation sending HOLDs at `C` and fails at `A,B,D`, that
nm2oricycy Orient reverse fails without being this sending, that
leftover-axis reverse fails because `A` has no opposite pair and lex-one
reverse HOLDs from `e1<e2<e3` order independent of `m`, that split fail is
transport fail not `UNDEFINED`, that empty `O_next` or empty `O_prev` is
Orient fail not `UNDEFINED`, that the 1-axis opposite two-site seed is a
different member with `t(B)=2` and cover face HOLD, that #7477 same-lock
is a different member with face transport fail, that LIVE three-axis as a
three-site seed is a different member with reverse transport fail, that
leftover-empty fail is a different predicate, that leftover of `M` alone
and leftover of `O` alone are different objects, that mixed sets remain
sets, that the construction does not sum, that a formation member from
already-recorded six-neighbor locks is not attached, that the second pair
is a new seed not a formed child, that the z-probes and x-probes of this
seed are not this letter, and that the display is not the two-tick
lock-count clock composition. No runner cache is written.
