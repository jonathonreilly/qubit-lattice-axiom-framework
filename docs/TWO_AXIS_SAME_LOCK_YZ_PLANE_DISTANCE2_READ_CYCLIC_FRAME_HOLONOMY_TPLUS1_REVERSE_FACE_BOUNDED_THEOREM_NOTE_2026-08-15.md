---
claim_id: two_axis_same_lock_yz_plane_distance2_read_cyclic_frame_holonomy_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Distance-2 read of yz-plane cyclic-frame holonomy at t+1 on the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_yz_plane_distance2_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py
---

# Distance-2 Read Of Yz-Plane Cyclic-Frame Holonomy At t+1 Reverse And Face On The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** distance-2 read of cyclic-frame holonomy around the yz-plane unit
square of simultaneous earliest incoming set `M` and outgoing dual `O` at
each vertex's `τ=t+1`, and reverse/face from that distance-2 read, on the
two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. `F` and Orient as
nm2cycfrmhol. Yz squares as nm2holyzsl. Holonomy as nm2holyzsl. Distance-2
read as nm2yzrdn2. Reverse yz
square at `x=0`: `A=(0,0,0)`, `D=(0,1,0)`, `B=(0,1,1)`, `E=(0,0,1)`. Face
yz square at `x=1`: `C=(1,0,0)`, `C1=(1,1,0)`, `C2=(1,1,1)`, `C3=(1,0,1)`
that lie in `B_3(0)`. Drop any vertex outside `B_3(0)` as fail, not
`UNDEFINED`. Let
`t(q)` be the formation tick of vertex `q`. Let `τ(q)=t(q)+1`. `M(q,τ)`
is the set of earliest incoming nearest-neighbor steps at `q` using only
records with tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is
the outgoing dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that
`q+e` is formed and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`.
Empty `O` is empty, not `UNDEFINED`. Axis of a defined lock set `S` is
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
HOLDs, `F(q)=(m,o_next,o_prev)` is an oriented lattice frame. For an edge
`q→r` of a formed six-neighbor pair, `P(q,r)` is the unique 3×3 signed
permutation with `det = Orient(q)Orient(r)` sending columns of `F(q)` to
columns of `F(r)`; if none, that edge fails. Holonomy of a square is the
matrix product `P12 P23 P34 P41`. Holonomy HOLDs if and only if every
vertex split HOLDs, every Orient is `±1`, every edge has `P`, and the
product is the 3×3 identity. Distance-2 read HOLDs at a square `S` if and
only if holonomy(`S`) HOLDs and some formed 6-NN translate of a formed
6-NN translate of `S` (graph distance 2, in `B_3(0)`) has holonomy HOLD.
Graph distance 2 is two successive formed six-neighbor square shifts
whose net shift has graph-length 2. If holonomy fails at `S`,
distance-2 read fails, not `UNDEFINED`. Reverse HOLDs if and only if
distance-2 read of the `x=0` yz square `A-D-B-E` HOLDs. Face HOLDs if and
only if distance-2 read of the `x=1` yz square `C-C1-C2-C3` HOLDs. Face is
displayed, not adopted. Cover and split do not score handedness. This is
not leftover of nm2holyz yz-square holonomy reverse HOLD face fail: those
holonomy bits are reverse HOLD and face fail on the two-axis opposite
seed, while this reverse fails and this face fails on the two-axis
same-lock seed. nm2holyz scores the product at `S` alone. This reverse
fails because holonomy at the reverse square fails from split fail at
`E`, even though the `−e_3` translate has holonomy HOLD. This is not
leftover of nm2yzrdn2 distance-2 read of yz holonomy fail/fail: nm2yzrdn2
is the same distance-2 letter on the two-axis opposite seed, where
holonomy of the reverse square HOLDs and reverse still fails because no
formed graph-distance-2 translate has holonomy HOLD; here same-lock
holonomy itself fails. This is not leftover of nm2holyzrd neighbor-read of
yz holonomy reverse HOLD face fail: nm2holyzrd reverse HOLDs on the
two-axis opposite seed from identity holonomy and the `±e_3` translates.
This is not leftover of nm2yzrdsl neighbor-read of yz holonomy fail/fail
on this same-lock seed: that reverse fails at graph distance 1 because
holonomy at `S` fails, while this letter is graph distance 2. This is not
leftover of nm2rdholfz neighbor-read of xy holonomy fail/fail: that reverse
fails and that face fails on a three-axis far-face seed, while this
fail/fail is the two-axis same-lock yz square. This is not leftover of nm2cycfrmhol
xy-square holonomy reverse HOLD face fail on the xy-plane square
`A-D-B-E` at `z=1`: that product is the identity and that face fails on
different vertices. This is not leftover of nm2cycfrmz cyclic-frame
transport reverse HOLD face HOLD: transport is existential at a vertex,
holonomy is the product around a square. On this same-lock seed transport
reverse fails at z-probe `A` while a mutation that scored only a
holonomy-HOLDING 6-NN translate of the reverse square would HOLD reverse
from the `−e_3` translate. Transport face HOLDs on the z-probes while
holonomy face of this yz square fails. This is not leftover of
nm2oricyclz cyclic Orient reverse HOLD whose bits are equal `±1` signs,
not a four-edge product. This is not leftover of scalar neighbor-read of
Orient. This is not leftover of a unique nonnegative permutation sending.
This is not leftover of nm2orichz leftover-axis reverse HOLD whose face
fails because C and D swap `(m,pair)` columns: those signs are not the
holonomy product, and holonomy reverse fails from split fail at `E`. This
is not leftover of nm2orionez lex-one reverse fail whose face HOLDs from
`e1<e2<e3` order independent of `m`. This is not leftover of nm2chiralz
lexicographic unsigned `o1,o2` orientation. This is not leftover of
nm2oridetz unique signed outgoing letters. This is not leftover of nm2axz
axis-cover. This is not leftover of nm2ax12z 1-in 2-out split. This is not
leftover of leftover-of-`M` alone. This is not leftover of leftover-of-`O`
alone. This is not leftover-empty fail of leftover axis. This is not
leftover of nmunopp union. This is not leftover of nmt2opp `M` frozen at
`t`. This is not leftover of nmot2opp two-tick composition. This is not
leftover of nmoutopp untimed eventual-`O`. This is not leftover of mixed
#7188 fail/fail. This is not leftover of the 1-axis opposite two-site
seed. This is not leftover of the same-lock two-site seed. Neither pair
is opposite. The second pair is a new seed, not a formed child.
Uniqueness is not required. Mixed remains a set. Displayed, not adopted.
Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the two named yz-plane unit squares. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-vertex cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev
lex-largest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m` and the
lex-largest signed outgoing letter on the cyclic next and prev axes of
`Axis(M)` under `+e < −e`. When split HOLDs, `F=(m,o_next,o_prev)` is
that LIVE three-axis frame. For a formed six-neighbor edge, `P` is the
unique signed permutation sending columns of `F(q)` to columns of `F(r)`
with determinant `Orient(q)Orient(r)`. Holonomy is the product of the four
edge matrices around the square. Distance-2 read of that holonomy HOLDs at a square if and only if the
square's holonomy HOLDs and some formed 6-NN translate of a formed 6-NN
translate in `B_3(0)` at graph distance 2 also has holonomy HOLD. Reverse
and face are scored on distance-2 read HOLD of the reverse square and of
the face square.
Holonomy of nm2holyz is a different readout: it scores the product at `S`
alone. Neighbor-read of xy holonomy on the three-axis far-face seed is a
different readout and fails reverse and face. Transport of nm2cycfrmz
is a different readout: it is existential at a vertex, not the product
around a square. Neighbor-read of the scalar Orient sign is a different
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
claim_type_reason: "Exact report of distance-2 read of cyclic-frame holonomy around the yz-plane unit square of M and O at t+1 on the two-axis same-lock seed, F and Orient at the eight square vertices, P on each edge, holonomy matrices, distance-2 read of those squares, reverse fail and face fail from distance-2 read of the two yz squares; uniqueness of a sending is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_yz_plane_distance2_read_cyclic_frame_holonomy_tplus1_reverse_face
target_blocker_text: "display distance-2 read of yz-plane cyclic-frame holonomy reverse/face on the two-axis same-lock seed, not nm2yzrdn2 opposite-seed distance-2, not nm2yzrdsl same-lock neighbor-read, not nm2holyz yz-square holonomy, not nm2holyzrd neighbor-read of yz holonomy on the opposite seed, not nm2rdholfz neighbor-read of xy holonomy, not nm2cycfrmhol xy-square holonomy, not nm2cycfrmz transport, not scalar neighbor-read of Orient, not unique nonnegative sending, not leftover-axis, not lex-one e1<e2<e3, not unique |O_i|=1, not unsigned axis units, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep distance-2 read of cyclic-frame holonomy of F around the yz-plane unit square at t+1 displayed; do not write holonomy into Admissibility, do not reduce to nm2yzrdn2 opposite-seed distance-2, do not reduce to nm2yzrdsl same-lock neighbor-read, do not reduce to nm2holyz yz-square holonomy, do not reduce to nm2holyzrd neighbor-read of yz holonomy on the opposite seed, do not reduce to nm2rdholfz neighbor-read of xy holonomy, do not reduce to nm2cycfrmhol xy-square holonomy, do not reduce to nm2cycfrmz transport, do not reduce to scalar neighbor-read of Orient, do not reduce to unique nonnegative permutation sending, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-smallest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace holonomy by unique outgoing letters, do not replace holonomy by existential opposite of signed locks, do not replace holonomy by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for distance-2 read of cyclic-frame holonomy around the yz-plane unit square of M and O at t+1 on the two-axis same-lock seed and reverse/face from that distance-2 read; displayed, not adopted"
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

No larger host is used. The reverse yz-plane unit square at `x=0` and the parallel face
square at `x=1` are the only cycles whose distance-2 read of cyclic-frame
holonomy of `F=(m,o_next,o_prev)` of `M` and `O` is scored:

```text
A = (0,0,0),  D = (0,1,0),  B = (0,1,1),  E = (0,0,1).
C = (1,0,0),  C1 = (1,1,0),  C2 = (1,1,1),  C3 = (1,0,1).
```

A vertex outside `B_3(0)` is fail, not `UNDEFINED`. These are not the
xy-plane square `A=(0,0,1)`, `D=(1,0,1)`, `B=(1,1,1)`, `E=(0,1,1)` of
nm2cycfrmhol. These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`,
`C=(0,2,0)`, `D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`,
`B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`. All four reverse vertices are
seeds of the two same-lock pairs. Same process as nm2axz. `F` and Orient
as nm2cycfrmhol.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `+e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `+e_2`. Neither pair is opposite. The second pair is
a new seed, not a formed child of the first pair. This seed is not the
two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` of nm2holyzrd. This
seed is not the 1-axis opposite two-site seed `{0,(0,1,0)}` with only
`+e_1/−e_1`. This seed is not the perp two-site seed `+e_1/+e_2`. This
seed is not the same-lock two-site seed `+e_1/+e_1`. This seed is not the
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

## Named cyclic-frame holonomy of `(m,o_next,o_prev)` at `τ=t+1`

Let `t(q)` be the formation tick of a square vertex `q` when that tick is
defined in `B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

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

Cyclic frame, edge sending, and holonomy at the same cut:

```text
When split HOLDs, F(q)=(m, o_next, o_prev).
For an edge q→r of a formed six-neighbor pair, P(q,r) is the
unique 3×3 signed permutation with det = Orient(q)Orient(r)
sending columns of F(q) to columns of F(r) (F(r)=F(q)P).
If none, that edge fails.
Holonomy of a square is P12 P23 P34 P41.
Holonomy HOLDs iff every vertex split HOLDs, every Orient is ±1,
every edge has P, and the product is the 3×3 identity.
If a vertex lies outside B_3(0), holonomy fails, not UNDEFINED.
If split or Orient fails at a vertex, holonomy fails, not UNDEFINED.
UNDEFINED if a vertex in the host is unformed at τ.
Distance-2 read HOLDs at a square S iff holonomy(S) HOLDs and some
formed 6-NN translate of a formed 6-NN translate of S (graph
distance 2, in B_3(0)) has holonomy HOLD.
Graph distance 2 is two successive formed six-neighbor square
shifts whose net shift has graph-length 2.
If holonomy fails at S, distance-2 read fails, not UNDEFINED.
Uniqueness of a sending neighbor is not required.
Uniqueness of a holonomy-HOLDING distance-2 translate is not required.
```

Neighbor-read of the scalar Orient sign HOLDs at `q` if and only if
`Orient(q)` is `±1` and some formed six-neighbor has the same sign. That
is a different object. Transport of nm2cycfrmz HOLDs at `q` if and only if
some formed six-neighbor hosts a signed-permutation sending. That is a
different object: on this same-lock seed transport fails at reverse vertex
`E` and at z-probe `A`, so transport reverse fails, while transport face
HOLDs on the z-probes. Holonomy of nm2holyzrd reverse HOLDs and holonomy
face fails on the two-axis opposite seed. Those opposite-seed bits are not
this same-lock fail/fail. A mutation that scored only a holonomy-HOLDING
6-NN translate, ignoring holonomy at `S`, would HOLD this reverse because
the `−e_3` translate has holonomy HOLD. Neighbor-read of xy holonomy on
the three-axis far-face seed fails reverse and face. A unique nonnegative
permutation sending is a different object and fails at each reverse
vertex. Transport of nm2cycfrmz on the z-probes reverse fails and face
HOLDs on this same-lock seed; leftover of that transport, not this
yz-square distance-2 read.

Reverse distance-2 read cyclic-frame holonomy holds if and only if
distance-2 read of the `x=0` yz square `A-D-B-E` HOLDs. Face distance-2
read cyclic-frame holonomy holds if and only if distance-2 read of the
`x=1` yz square `C-C1-C2-C3` HOLDs. If holonomy of a square fails,
distance-2 read of that square fails, not `UNDEFINED`.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover reverse fails at z-probe `A` as this reverse
fails, but cover face HOLDs while this face fails. Identifying split
reverse with this reverse is refused: split reverse fails at z-probe `A`
from `Axis(M)` meeting `Axis(O)`, while holonomy reverse fails from split
fail at reverse vertex `E`; split face HOLDs on z-probes `C,D` while
holonomy face fails at `C,C1` of the `x=1` yz square. Identifying
leftover-empty fail with this reverse is refused: leftover-empty fail
scores empty leftover as reverse fail and face fail, matching these bits
on a different object; leftover-empty also fails reverse on the opposite
seed, where nm2holyzrd reverse HOLDs. Identifying nm2holyz yz-square
holonomy with this reverse is refused: nm2holyz reverse HOLDs and face
fails from the product at `S` alone on the opposite seed. Identifying
nm2yzrdn2 distance-2 read of yz holonomy with this reverse is refused:
nm2yzrdn2 reverse fails after holonomy HOLDs on the opposite seed. Identifying
nm2yzrdsl neighbor-read of yz holonomy with this reverse is refused:
nm2yzrdsl reverse fails at graph distance 1 on this same-lock seed.
Identifying nm2holyzrd neighbor-read of yz holonomy with this reverse is
refused: nm2holyzrd reverse HOLDs and face fails on the two-axis opposite
seed; this reverse fails on same-lock. Identifying nm2rdholfz neighbor-read of
xy holonomy with this reverse is refused: that reverse fails and that
face fails on a three-axis far-face seed. Identifying nm2cycfrmhol
xy-square holonomy with this reverse is refused: that reverse HOLDs and
that face fails on different vertices. Identifying nm2cycfrmz transport
with this reverse is refused: transport reverse fails as this reverse
fails, but transport face HOLDs on the z-probes while this face fails.
Identifying lexicographic unsigned `o1,o2` with this reverse is refused:
unsigned reverse fails and unsigned face HOLDs. Identifying nm2orionez
lex-one signed `e1<e2<e3` with this reverse is refused: lex-one reverse
fails from axis order independent of `m`; lex-one face HOLDs while this
face fails. Identifying unique signed `|O_i|=1` with this reverse is
refused: unique signed reverse fails as this reverse fails, from
`|O_i|≠1`, not from split fail at `E`. Identifying leftover-axis
orientation with this reverse is refused: leftover-axis reverse fails at
z-probe `A` on this seed; leftover-axis face fails because C and D swap
`(m,pair)` columns; those two signs are not the holonomy product of four
edge sendings. Identifying cyclic lex-smallest with this reverse is
refused: lex-smallest picks `+e` if both signs. Identifying a named sign
of those locks with reverse or face is refused: named-sign lettering lost
the axis.

## Theorem 1 — ticks, `F`, Orient, `P` on each edge, holonomy, distance-2 read

On this process the eight square vertices form in `B_3(0)`. Compare to
leftover axis: that leftover reports empty leftover at `A,B,C,D` and leftover
reverse fail and leftover face fail. Compare to nm2axz cover and nm2ax12z
split: both HOLD reverse and face on `A,B,C,D`. Compare to nm2oricyclz cyclic
Orient: reverse HOLDs and face HOLDs from equal `±1` signs without a
four-edge product. Compare to nm2cycfrmz cyclic-frame transport: reverse
HOLDs and face HOLDs from existential sendings at `A,B,C,D`. Compare to
scalar neighbor-read of Orient: HOLD at `A` and fail at `B`, `C`, and `D`.
Compare to nm2chiralz lexicographic unsigned `o1,o2` orientation: reverse
fails and face HOLDs. Compare to nm2oridetz unique signed outgoing letters:
reverse fails and face fails because `|O_i|≠1`. Compare to nm2orichz
leftover-axis reverse HOLD whose face fails because C and D swap `(m,pair)`
columns. Compare to nm2orionez lex-one reverse fail whose face HOLDs from
`e1<e2<e3` order independent of `m`. This display reads distance-2 read of the cyclic-frame
holonomy of `(m,o_next,o_prev)` around the two yz-plane unit squares of
those same timed sets:

```text
t(A)=0
t(D)=0
t(B)=0
t(E)=0
t(C)=2
t(C1)=2
t(C2)=1
t(C3)=1
M(A, τ) = {+e_1}
M(B, τ) = {+e_2}
M(C, τ) = {−e_3}
M(D, τ) = {+e_1}
M(E, τ) = {+e_2}
M(C1, τ) = {−e_3}
M(C2, τ) = {+e_1}
M(C3, τ) = {+e_1}
O(A, τ) = {−e_2, −e_3}
O(B, τ) = {+e_1, −e_1, +e_3}
O(C, τ) = {+e_1}
O(D, τ) = {+e_2, −e_3}
O(E, τ) = {+e_1, −e_1, +e_2, +e_3}
O(C1, τ) = {+e_1}
O(C2, τ) = {+e_2, +e_3, −e_3}
O(C3, τ) = {−e_2, +e_3, −e_3}
split(A) = hold
split(B) = hold
split(C) = fail
split(D) = hold
split(E) = fail
split(C1) = fail
split(C2) = hold
split(C3) = hold
m(A) = +e_1
i(A) = 1
o_next(A) = −e_2
o_prev(A) = −e_3
det(A) = 1
Orient(A) = +1
m(B) = +e_2
i(B) = 2
o_next(B) = +e_3
o_prev(B) = −e_1
det(B) = -1
Orient(B) = −1
m(D) = +e_1
i(D) = 1
o_next(D) = +e_2
o_prev(D) = −e_3
det(D) = -1
Orient(D) = −1
Orient(E) = fail
Orient(C) = fail
Orient(C1) = fail
Orient(C2) = −1
Orient(C3) = +1
F(A) = (+e_1, −e_2, −e_3)
F(B) = (+e_2, +e_3, −e_1)
F(C) = fail
F(D) = (+e_1, +e_2, −e_3)
F(E) = fail
F(C1) = fail
F(C2) = (+e_1, +e_2, −e_3)
F(C3) = (+e_1, −e_2, −e_3)
P(A→D) = [1 0 0; 0 -1 0; 0 0 1]
P(D→B) = [0 0 -1; 1 0 0; 0 -1 0]
P(B→E) = fail
P(E→A) = fail
holonomy(A-D-B-E) = fail
P(C→C1) = fail
P(C1→C2) = fail
P(C2→C3) = [1 0 0; 0 -1 0; 0 0 1]
P(C3→C) = fail
holonomy(C-C1-C2-C3) = fail
holonomy(A-D-B-E + e_1) = fail
holonomy(A-D-B-E − e_1) = fail
holonomy(A-D-B-E + e_2) = fail
holonomy(A-D-B-E − e_2) = fail
holonomy(A-D-B-E + e_3) = fail
holonomy(A-D-B-E − e_3) = hold
holonomy(C-C1-C2-C3 + e_1) = fail
holonomy(C-C1-C2-C3 − e_1) = fail
holonomy(C-C1-C2-C3 + e_2) = fail
holonomy(C-C1-C2-C3 − e_2) = fail
holonomy(C-C1-C2-C3 + e_3) = fail
holonomy(C-C1-C2-C3 − e_3) = fail
neighbor-read(A-D-B-E) = fail
neighbor-read(C-C1-C2-C3) = fail
distance-2 read(A-D-B-E) = fail
distance-2 read(C-C1-C2-C3) = fail
```

`A` is a seed at tick 0 with seed letter `+e_1`. All four reverse vertices
are seeds: `t(A)=t(D)=t(B)=t(E)=0`. Mixed remains a set: `O(B,τ)` has
three outgoing steps and `O(E,τ)` has four outgoing steps. Unique
outgoing letters would assign `UNDEFINED` at mixed `O`. Unique signed
`|O_i|=1` fails at `B` because `O(B)` has both `±e_1`. Split fails at `E`
because `Axis(M)={e_2}` meets `Axis(O)={e_1,e_2,e_3}`: the outgoing dual
contains the incoming axis `+e_2`. Cover and split do not score
handedness. At `A`, `i=1` so `e_next=e_2` and `e_prev=e_3`; `O` is
`{−e_2,−e_3}` with no opposite pair. At `C`, `m=−e_3` so `i=3`,
`e_next=e_1`, `e_prev=e_2`; `O={+e_1}` leaves `O_prev` empty, so Orient
fails, not `UNDEFINED`. At `C1`, `O={+e_1}` still leaves `O_prev` empty.
O is not M.

On the 1-axis opposite two-site seed, `E=(0,0,1)` is a formed child at
tick 1 locking `+e_3`, and this reverse square is not four seeds. That is
leftover of the first pair. Here both `(0,0,1)` and `(0,1,1)` are seeds of
a second same-lock pair on a second axis, and origin and `(0,1,0)` are the
first same-lock pair. This reverse square is exactly those four seeds. On
the two-axis opposite seed of nm2holyzrd, reverse neighbor-read HOLDs and
face fails. On the xy-plane square of nm2cycfrmhol, reverse HOLDs and face
fails from 2-in split fail at height 2; those vertices are not this yz
square. On the y-probes of this same seed, y-probe reverse HOLDs while
this yz reverse fails.

New records in `B_3(0)` between `t` and `t+1` that meet a vertex's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,0)` is a
seed, so it is not a new 6-NN of `A`:

```text
new 6-NN of A at t(A)+1: (0, -1, 0), (0, 0, -1)
new 6-NN of B at t(B)+1: (1, 1, 1), (-1, 1, 1), (0, 1, 2)
new 6-NN of C at t(C)+1: (2, 0, 0)
new 6-NN of D at t(D)+1: (0, 2, 0), (0, 1, -1)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at `A`, `D`, and
`B`; at `E`, `O` at `t` is `{+e_2}`. Split fails at `t`, Orient is fail,
not UNDEFINED, and the cyclic frame fails, not UNDEFINED. Transport at
`t` therefore fails, not UNDEFINED.

Uniqueness of a sending neighbor is not required. `P(A→D)` and `P(D→B)`
exist as signed permutations, but `P(B→E)` and `P(E→A)` fail because
split fails at `E`. Reverse-square holonomy therefore fails, not
`UNDEFINED`. The `−e_3` translate of the reverse square has holonomy
HOLD, so a mutation that ignored holonomy at `S` would HOLD reverse at
graph distance 1; distance-2 read still fails because holonomy at the
reverse square itself fails. Face-square holonomy fails because `C` and
`C1` are split fail, so distance-2 read of the face square fails, not
`UNDEFINED`. No formed 6-NN translate of the face square has holonomy
HOLD. The `−e_1` translate of the face square is the reverse square, whose
holonomy also fails. This is not leftover of nm2yzrdn2: that reverse fails
after holonomy of the reverse square HOLDs on the opposite seed. This is
not leftover of nm2yzrdsl: that neighbor-read reverse fails at graph
distance 1 on this same seed. This is not leftover of nm2holyzrd: that
reverse HOLDs on the opposite seed. This is not leftover of nm2holyz: that
scores the product at `S` alone. This is not leftover of nm2rdholfz: that
reverse fails and that face fails on a three-axis far-face seed. This is
not leftover of nm2cycfrmhol: that face fails at `z=2` 2-in vertices, while
this reverse fails at `E` on the `x=0` yz square.

The 3-split is a field: opposite Orient at a neighbor is allowed when
`det(P)` equals the product of the two signs.

## Theorem 2 — reverse from distance-2 read of cyclic-frame holonomy at `τ`

Reverse distance-2 read cyclic-frame holonomy holds if and only if
distance-2 read of the `x=0` yz square `A-D-B-E` HOLDs. Split fails at `E`
because `O(E)` contains the incoming axis `+e_2`, so `P(B→E)` and
`P(E→A)` fail, holonomy of the reverse square fails, and distance-2 read
therefore fails, not `UNDEFINED`. The formed 6-NN translate by `−e_3`
has holonomy HOLD; that neighbor is not enough, because holonomy at the
reverse square itself fails. Reverse fails. This is fail iff holonomy of
the reverse square fails, not leftover of nm2yzrdn2 distance-2 read of yz
holonomy, not leftover of nm2yzrdsl neighbor-read of yz holonomy, not
leftover of nm2holyz yz-square holonomy, not leftover of nm2holyzrd
neighbor-read of yz holonomy, not leftover of nm2rdholfz neighbor-read of
xy holonomy, not leftover of nm2cycfrmhol xy-square holonomy, not leftover
of nm2cycfrmz cyclic-frame transport, not leftover of nm2oricyclz cyclic
Orient equal signs, not leftover of scalar neighbor-read, not leftover of
a unique nonnegative permutation sending, not leftover of nm2chiralz
lexicographic unsigned `o1,o2`, not leftover of nm2oridetz unique signed
outgoing letters, not leftover of nm2orichz leftover-axis, not leftover of
nm2orionez lex-one, not leftover of nm2axz axis-cover, not leftover of
nm2ax12z 1-in 2-out split, not leftover-empty fail, and not exist-opposite.

Reverse distance-2 read cyclic-frame holonomy at τ: fail

Both squares are defined, so this is not `UNDEFINED`. Cover reverse fails
because cover fails at z-probe `A`. Split reverse fails because split
fails at z-probe `A`. Cover and split do not score handedness.
nm2cycfrmz transport reverse fails because transport fails at z-probe
`A`; that is existential at two vertices, not the four-edge product. On
the opposite seed, nm2holyzrd reverse HOLDs. Leftover-axis reverse fails
at z-probe `A`, but leftover-axis is two signs, not `P12 P23 P34 P41`.
Lexicographic unsigned reverse fails. Unique signed reverse fails because
both unique signed signs fail. Lex-one signed reverse fails because
lex-one `Orient(A)` fails. Cyclic lex-smallest reverse fails. Leftover-empty
reverse fails because leftover of the union is empty at z-probes `A` and
`B`. Leftover-empty also fails reverse on the opposite seed, where
nm2holyzrd reverse HOLDs. Leftover of `M` reverse fails because leftover
of `M` at `A` is `{e_1, e_3}` and at `B` is `{e_2, e_3}`: nonempty and
unequal. Leftover of `O` reverse fails because leftover of `O` at `A` is
empty and at `B` is `{e_1}`. Exist-opposite reverse of signed `M` fails.
Exist-opposite reverse of signed `O` holds, while this reverse fails.
Presence of an opposite pair in `O` at z-probes `A` and `B` HOLDs. Those
leftovers are not this display.

Reverse fails.

## Theorem 3 — face from distance-2 read of cyclic-frame holonomy at `τ`

Face distance-2 read cyclic-frame holonomy holds if and only if
distance-2 read of the `x=1` yz square `C-C1-C2-C3` HOLDs. Split fails at
`C` and at `C1` because `O_prev` is empty on the cyclic prev axis of
`m=−e_3`, so `P(C→C1)`, `P(C1→C2)`, and `P(C3→C)` fail, holonomy of the
face square fails, and distance-2 read therefore fails, not `UNDEFINED`.
The `−e_1` translate of the face square is the reverse square and also
has holonomy fail. No formed 6-NN translate of the face square has
holonomy HOLD. Face fails. Displayed, not adopted.

Face distance-2 read cyclic-frame holonomy at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face HOLDs on the z-probes because cover HOLDs at those `C` and
`D`. Split face HOLDs on the z-probes. Those z-probes are not this yz face
square: holonomy face reads `C,C1,C2,C3` at `x=1`, and split fails at `C`
and `C1`. Cyclic lex-largest oriented face HOLDs on the z-probes because
both signs there are `+1`; that pair is not the four-edge product.
nm2cycfrmz transport face HOLDs on the z-probes; that existential pair is
not this holonomy. Leftover-axis face fails because those z-probe signs
are `+1` and `−1`: C and D swap `(m,pair)` columns. That face fail is two
leftover signs, not split fail at `C,C1`. Lex-one signed oriented face
HOLDs on the z-probes. Lexicographic unsigned face HOLDs on the z-probes.
Unique signed face fails on the z-probes because neither unique signed
sign is `±1`. Cover and split do not score handedness. Presence of an
opposite pair in `O` HOLDs at the z-probe face pair, so pair-presence face
HOLDs while this face fails. On the 1-axis opposite two-site seed, reverse
holonomy of this yz square HOLDs and face holonomy fails; here `t(A)=0`
and face holonomy fails at `C,C1`. The four y-probes of this same seed
give cyclic Orient `−1` at y-probe `A` and at y-probe `B`, so y-reverse
HOLDs, while this yz reverse fails; y-face fails from Orient fail at
y-probe `D`. The four x-probes give oriented reverse fail and oriented
face fail. Those probe-direction readouts are not this yz-plane
unit-square holonomy. Leftover-empty face fails on the z-probes because
leftover of the union is empty there. Exist-opposite face of signed `M`
fails. Exist-opposite face of signed `O` fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse: leftover-empty also fails reverse on the opposite seed,
where nm2holyzrd reverse HOLDs. Cover HOLDs at reverse `D` and split HOLDs
at reverse `D`. Orient at reverse `D` is `−1` from cyclic `(+e_2,−e_3)`.
A vertex outside `B_3(0)`, for example the parallel yz square at `x=4`,
is holonomy fail, not `UNDEFINED`.

Face fails.

## What this note does not claim

- It does not replace distance-2 read by nm2yzrdn2 opposite-seed distance-2.
- It does not replace distance-2 read by nm2yzrdsl same-lock neighbor-read.
- It does not replace distance-2 read by nm2holyz yz-square holonomy.
- It does not replace distance-2 read by nm2holyzrd neighbor-read of yz holonomy.
- It does not replace distance-2 read by nm2rdholfz neighbor-read of xy holonomy.
- It does not replace holonomy by nm2cycfrmz cyclic-frame transport.
- It does not replace holonomy by neighbor-read of the scalar Orient sign.
- It does not replace holonomy by a unique nonnegative permutation sending.
- It does not require a unique formed six-neighbor witness.
- It does not reprint nm2oricyclz cyclic Orient reverse hold face hold as this holonomy.
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
- It does not reprint nm2axz axis-cover reverse hold face hold as this
  oriented display.
- It does not reprint nm2ax12z 1-in 2-out split reverse hold face hold as
  this oriented display.
- It does not reprint nm2chiralz lexicographic unsigned `o1,o2` reverse fail
  face hold with `+1,+1` as this oriented display.
- It does not reprint nm2oridetz unique signed reverse fail face fail as
  this oriented display.
- It does not reprint nm2orichz leftover-axis reverse hold face fail as
  this oriented display.
- It does not reprint nm2orionez lex-one reverse fail face hold as this
  oriented display.
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

This display uses Lattice to name `B_3(0)` and the two unit squares. It uses
Qubit only as the algebra of the local possibility domain. It uses Record
only as a boundary: a present lock is content. It does not rewrite
Admissibility. The two-axis same-lock seed process, distance-2 read of
cyclic-frame holonomy of `(m,o_next,o_prev)` of `M` and `O` at `t+1` around
the unit square, and the reverse/face bits from that distance-2 read are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(D)`, `t(B)`, `t(E)`, `t(C)`, `t(C1)`, `t(C2)`, `t(C3)` | Theorem 1; `0`, `0`, `0`, `0`, `2`, `2`, `1`, `1` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; HOLD at `A,D,B,C2,C3`; fail at `E,C,C1` |
| unique signed `m`, axis index `i`, cyclic `(o_next,o_prev)` | Theorem 1; singleton `M` on reverse square; split fail at `E` |
| integer `det(m,o_next,o_prev)` | Theorem 1; reverse square `1`, `-1`, `-1`; fail at `E` |
| Orient at `τ` | Theorem 1; reverse `+1,−1,−1`, fail; face fail, fail, `−1`, `+1` |
| cyclic frame `F=(m,o_next,o_prev)` | Theorem 1; LIVE three-axis at `A,D,B`; fail at `E,C,C1` |
| `P` on each reverse edge | Theorem 1; `P(A→D)` and `P(D→B)` signed permutations; `P(B→E)` and `P(E→A)` fail |
| holonomy matrix of `A-D-B-E` | Theorem 1; fail |
| holonomy matrix of `C-C1-C2-C3` | Theorem 1; fail |
| neighbor-read of `A-D-B-E` | Theorem 1; fail because holonomy fails, even though the `−e_3` translate HOLDs; leftover of nm2yzrdsl |
| neighbor-read of `C-C1-C2-C3` | Theorem 1; fail because holonomy fails, not UNDEFINED |
| distance-2 read of `A-D-B-E` | Theorem 1; fail because holonomy fails, not UNDEFINED |
| distance-2 read of `C-C1-C2-C3` | Theorem 1; fail because holonomy fails, not UNDEFINED |
| leftover of nm2holyz yz-square holonomy | Theorem 1; holonomy reverse hold and holonomy face fail on the opposite seed without a translate test |
| leftover of nm2yzrdn2 distance-2 read of yz holonomy | Theorem 1; reverse fail after holonomy HOLD on the two-axis opposite seed |
| leftover of nm2yzrdsl neighbor-read of yz holonomy | Theorem 1; reverse fail at graph distance 1 on this same-lock seed |
| leftover of nm2holyzrd neighbor-read of yz holonomy | Theorem 1; reverse hold and face fail on the two-axis opposite seed |
| leftover of nm2rdholfz neighbor-read of xy holonomy | Theorem 1; reverse fail and face fail on a three-axis far-face seed |
| leftover of nm2cycfrmz cyclic-frame transport | Theorem 1; transport reverse fail and transport face hold on this seed; not this letter |
| reverse from distance-2 read of cyclic-frame holonomy at `τ` | Theorem 2; `fail` |
| face from distance-2 read of cyclic-frame holonomy at `τ` | Theorem 3; `fail` |
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
| leftover of nm2chiralz lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichz leftover-axis | not this oriented display |
| leftover of nm2orionez lex-one signed `e1<e2<e3` | not this oriented display |
| leftover of cyclic lex-smallest | not this oriented display |
| leftover of nm2oricyclz cyclic Orient equal signs | not this holonomy |
| leftover of nm2cycfrmz cyclic-frame transport | not this holonomy |
| leftover of nm2holyz yz-square holonomy | not this distance-2 read |
| leftover of nm2yzrdn2 opposite-seed distance-2 | not this same-lock seed |
| leftover of nm2yzrdsl same-lock neighbor-read | not this graph-distance-2 letter |
| leftover of nm2holyzrd neighbor-read of yz holonomy | not this same-lock seed |
| leftover of nm2rdholfz neighbor-read of xy holonomy | not this yz square |
| leftover of scalar neighbor-read of Orient | not this transport |
| leftover of unique nonnegative permutation sending | not this transport |
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
| leftover of the same-lock two-site seed | not this display; #7477 same-lock two-site reverse neighbor-read HOLDs |
| leftover of the two-axis opposite seed | not this display; nm2holyzrd reverse HOLDs |
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
| V1 | It answers the first-display question: distance-2 read of cyclic-frame holonomy around the yz-plane unit square of `(m,o_next,o_prev)` of `M` and `O` at `t+1` on the two-axis same-lock seed, and reverse/face from that distance-2 read. |
| V2 | Current main has no landed distance-2 read of yz-plane cyclic-frame-holonomy reverse/face of timed `M` and `O` on these two yz-plane unit squares of the two-axis same-lock seed. |
| V3 | Edge sendings, two holonomy matrices, distance-2 read of those squares, and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads distance-2 read of the four-edge signed-permutation product around a unit square at the same `t+1` cut, reverse fails and face fails while nm2yzrdn2 reverse fails after holonomy HOLDs on the opposite seed, nm2yzrdsl neighbor-read reverse fails at graph distance 1 on this seed, nm2holyzrd neighbor-read reverse HOLDs and face fails on the opposite seed, nm2holyz holonomy reverse HOLDs and holonomy face fails from the product at `S` alone, a mutation ignoring holonomy at `S` would HOLD reverse from the `−e_3` translate, nm2rdholfz neighbor-read of xy holonomy reverse fails and face fails, nm2cycfrmz transport reverse fails and transport face HOLDs, scalar neighbor-read reverse fails, unique nonnegative sending fails at each of `A,B,C,D`, and nm2oricyclz Orient equality does not supply the product. |
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
nmcover axis-cover, does not replace Orient by nm2axz axis-cover, does not
replace Orient by nm2ax12z 1-in 2-out split, does not identify this
display with the 1-axis opposite two-site seed, and does not identify it
with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| scalar neighbor-read of Orient | reuse equal Orient sign at some formed 6-NN | scalar reverse fails and scalar face fails as this reverse fails and this face fails, from equal signs not a four-edge product | ATTEMPTED |
| unique nonnegative permutation sending | require a unique sending with no minus signs | unique nonnegative sending fails at each of `A,B,C,D`; uniqueness is not required | ATTEMPTED |
| nm2holyz yz-square holonomy | reuse holonomy reverse hold and face fail of the opposite two-axis yz squares | nm2holyz reverse HOLDs and face fails from the product at `S` alone on the opposite seed; this reverse fails even though the `−e_3` translate has holonomy HOLD | ATTEMPTED |
| nm2yzrdn2 opposite-seed distance-2 | reuse distance-2 reverse fail and face fail | nm2yzrdn2 reverse fails after holonomy of the reverse square HOLDs; here holonomy itself fails | ATTEMPTED |
| nm2yzrdsl same-lock neighbor-read | reuse neighbor-read reverse fail and face fail | nm2yzrdsl reverse fails at graph distance 1 on this seed; this letter is graph distance 2 | ATTEMPTED |
| nm2holyzrd neighbor-read of yz holonomy | reuse neighbor-read reverse hold and face fail | nm2holyzrd reverse HOLDs and face fails on the two-axis opposite seed; this reverse fails on same-lock | ATTEMPTED |
| nm2rdholfz neighbor-read of xy holonomy | reuse neighbor-read reverse fail and face fail | nm2rdholfz reverse fails and face fails on a three-axis far-face seed; this fail/fail is the two-axis same-lock yz square | ATTEMPTED |
| nm2cycfrmhol xy-plane holonomy | reuse holonomy reverse hold and face fail of `A-D-B-E` at `z=1` | that reverse HOLDs and that face fails on different vertices; this reverse fails at `E` on the `x=0` yz square of four same-lock seeds | ATTEMPTED |
| nm2cycfrmz cyclic-frame transport | reuse transport reverse fail and face hold from existential 6-NN sendings | transport reverse fails as this reverse fails, but transport face HOLDs while this face fails; transport is existential at a vertex, holonomy is the four-edge product | ATTEMPTED |
| nm2oricyclz cyclic Orient | reuse Orient reverse hold and face hold from equal `±1` signs | Orient reverse fails at z-probe `A` and face HOLDs without a four-edge product; HOLDING cyclic #7451/#7452 is the frame sign, not holonomy | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face hold | unsigned reverse fails as this reverse fails; unsigned face HOLDs while this face fails | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed reverse fails as this reverse fails, from `|O_i|≠1`, not from split fail at `E` | ATTEMPTED |
| nm2orichz leftover-axis | reuse leftover-axis reverse fail and face fail | leftover-axis reverse fails at z-probe `A`; leftover-axis face fails because C and D swap `(m,pair)` columns; those two signs are not `P12 P23 P34 P41` | ATTEMPTED |
| nm2orionez lex-one | reuse lex-one reverse fail and face hold | lex-one reverse fails from `e1<e2<e3` order independent of `m`; lex-one face HOLDs while this face fails | ATTEMPTED |
| cyclic lex-smallest | reuse same cyclic axes with `+e` if both signs | lex-smallest reverse fails and face HOLDs with `−1,−1`; this reverse fails from holonomy fail at `E` and this face fails | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse fail and cover face hold on these z-probes | cover reverse fails at z-probe `A`; cover face HOLDs while this face fails; Cover and split do not score handedness | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse split reverse fail and split face hold | split reverse fails at z-probe `A`; split face HOLDs while this face fails; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails as this reverse fails, and leftover-empty also fails reverse on the opposite seed where nm2holyzrd reverse HOLDs | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal; leftover of `M` reverse fails as this reverse fails, from a different object | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is empty and at `B` is `{e_1}`, unequal | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `O` holds while this reverse fails; exist-opposite face of signed `O` fails as this face fails, from a different object | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence HOLDs at each of `A,B,C,D` without cyclic columns; pair-presence face HOLDs while this face fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-largest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(E,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient at `E` is fail from split | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member both agree; flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient from `+1` to `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, Orient fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=0` and the reverse yz square is four seeds | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe reverse HOLDs (`−1,−1`) and y-face fails; this yz reverse fails | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the yz-plane unit square | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-largest outgoing determinant orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face fail on the same-lock yz-plane unit square | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; two-site same-lock reverse neighbor-read HOLDs; this member is two disjoint same-lock pairs | ATTEMPTED |
| two-axis opposite seed | reuse `+e_1/−e_1` and `+e_2/−e_2` | different seed; nm2holyzrd reverse HOLDs; neither pair is opposite here | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(E)` sums to `+e_2++e_3` while split fails | ATTEMPTED |
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
nmcover axis-cover, missing identification of Orient with nm2axz axis-cover,
missing identification of Orient with nm2ax12z 1-in 2-out split, missing
identification of this seed with the 1-axis opposite two-site seed, and
missing Record identification of Orient reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock seed pairs `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
next/prev axes of `Axis(M)`, lex-largest signed outgoing letter under
`+e < −e` (hence `−e` if both signs), integer determinant sign, empty
`O_next` or empty `O_prev` as Orient fail not `UNDEFINED`, split fail as
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
| per element | cyclic frame `F=(m,o_next,o_prev)` and signed-permutation sending to a formed 6-NN | no continuum alphabet |
| per site | reverse yz square `A-D-B-E` at `x=0` and face yz square `C-C1-C2-C3` at `x=1` on Euclidean `B_3(0)`; no other sites | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | edge sendings, two holonomy matrices, distance-2 read of those squares, reverse/face from distance-2 read | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for distance-2 read of
cyclic-frame holonomy reverse/face, a formation-rate rule, and a physical
selector among 1-in 2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Distance-2 reverse fail and face fail are only leftover of
nm2yzrdn2 opposite-seed distance-2, or of nm2yzrdsl same-lock neighbor-read,
or of nm2holyzrd neighbor-read of yz holonomy, or of nm2holyz yz-square
holonomy, or of nm2rdholfz neighbor-read of xy holonomy, or of nm2cycfrmz
cyclic-frame transport, or of leftover-empty fail, or of unique signed
`|O_i|=1`; same-lock already kills reverse of transport, so this reverse
fail is only that transport fail; mixed #7188 already reported fail/fail;
the second pair is only the formed child `(0,0,1)` of the 1-axis seed;
unique outgoing letters should be required; and a mutation that scored
only a holonomy-HOLDING translate already answers reverse.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail, matching these bits on a different object: leftover-empty
also fails reverse on the opposite seed, where nm2holyzrd reverse HOLDs.
Distance-2 reverse fails because holonomy of the `x=0` yz square
`A-D-B-E` fails from split fail at `E`, even though the formed 6-NN
translate by `−e_3` has holonomy HOLD. Distance-2 face fails because
holonomy of the `x=1` square fails from split fail at `C` and at `C1`,
and no formed translate has holonomy HOLD. nm2yzrdn2 reverse fails after
holonomy HOLDs on the opposite seed. nm2yzrdsl neighbor-read reverse fails
at graph distance 1 on this seed. nm2holyzrd reverse HOLDs on the
two-axis opposite seed. nm2holyz scores the product at `S` alone.
nm2rdholfz reverse fails and face fails on a three-axis far-face seed.
Transport reverse fails as this reverse fails, but transport face HOLDs
on the z-probes while this face fails: leftover of nm2cycfrmz cyclic-frame
transport, not this holonomy. Same-lock kills reverse of transport and
also kills reverse of this distance-2 read, from different objects.
nm2cycfrmhol xy-square holonomy reverse HOLDs and face fails on different
vertices. Unique nonnegative permutation sending fails at each reverse
vertex. Cover reverse fails at z-probe `A`; cover face HOLDs while this
face fails. Split reverse fails at z-probe `A`; split face HOLDs while
this face fails. Cover and split do not score handedness. Exist-opposite
reverse of signed `O` HOLDs while this reverse fails. Unique outgoing
letters would assign `UNDEFINED` at mixed `O(E)`; this Orient at `E` is
fail from split, not `UNDEFINED`. Mixed #7188 is a different z-symmetric
process with mixed `M`. The second pair is a new seed, not a formed child:
`(0,0,1)` is recorded at tick 0 with lock `+e_2`, whereas the 1-axis child
forms at tick 1 with lock `+e_3`. Neither pair is opposite.

### N8 — cross-cycle echo

nm2axz cover on this two-axis seed reported cover HOLD at each of the four
z-probes, reverse hold, and face hold. nm2ax12z 1-in 2-out split on the
same seed reported split HOLD at each of the four z-probes, reverse hold,
and face hold. nm2chiralz lexicographic unsigned `o1,o2` on the same seed
reported Orient `−1,+1,+1,+1`, reverse fail, and face hold. nm2oridetz
unique signed outgoing letters on the same seed reported Orient fail at
each probe, reverse fail, and face fail. nm2orichz leftover-axis on the
same seed reported Orient `−1,−1,+1,−1`, reverse hold, and face fail
because C and D swap `(m,pair)` columns. nm2orionez lex-one on the same
seed reported Orient `−1,+1,−1,−1`, reverse fail, and face hold from
`e1<e2<e3` order independent of `m`. Leftover axis reported empty leftover
at each of four z-probes, leftover reverse fail, and leftover face fail.
The four y-probes of this same seed reported cyclic Orient `−1` at `A`
and at `B`, so y-reverse HOLDs, and Orient fail at `D` from split fail, so
y-face fails. nm2oricyclz cyclic next/prev lex-largest Orient on the
z-probes of this seed reports Orient fail at `A` and face hold from equal
`+1,+1` signs at `C,D`, without a sending matrix. This note is not those
displays: it reports distance-2 read of cyclic-frame holonomy of
`(m,o_next,o_prev)` of `M` and `O` at `τ=t+1` around the yz-plane unit
square on the two-axis same-lock seed, with `t(A)=0`, `t(D)=0`, `t(B)=0`,
`t(E)=0`, `t(C)=2`, `t(C1)=2`, `t(C2)=1`, and `t(C3)=1`, reverse
distance-2 read fail, and face distance-2 read fail, while nm2yzrdn2
distance-2 reverse fails after holonomy HOLDs on the opposite seed, while
nm2yzrdsl neighbor-read reverse fails at graph distance 1 on this seed,
while nm2holyzrd neighbor-read of yz holonomy reverse HOLDs and face fails
on the opposite seed, while nm2holyz yz-square holonomy reverse HOLDs and
face fails from the product at `S` alone, while nm2rdholfz neighbor-read
of xy holonomy reverse fails and face fails, while nm2cycfrmhol xy-square
holonomy also reverse HOLDs and face fails on different vertices, while
nm2cycfrmz transport reverse fails and transport face HOLDs on the
z-probes. Cover and split do not score handedness.

**Gate disposition:** PASS for the distance-2-read cyclic-frame-holonomy
`t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the predicate
equals the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals nm2chiralz lexicographic unsigned `o1,o2`
HOLD,” “the predicate equals nm2oridetz unique signed HOLD,” “the
predicate equals nm2orichz leftover-axis HOLD,” “the predicate equals
nm2orionez lex-one HOLD,” “the predicate equals cyclic lex-smallest HOLD,”
“the predicate equals nm2oricyclz cyclic Orient HOLD,” “the predicate
equals nm2cycfrmz cyclic-frame transport HOLD,” “the predicate equals
nm2holyz yz-square holonomy HOLD,” “the predicate equals nm2yzrdn2
opposite-seed distance-2 HOLD,” “the predicate equals nm2yzrdsl
same-lock neighbor-read HOLD,” “the predicate equals nm2holyzrd
neighbor-read of yz holonomy HOLD,” “the predicate equals nm2rdholfz
neighbor-read of xy holonomy HOLD,” “the predicate equals
scalar neighbor-read of Orient HOLD,” “the predicate equals unique
nonnegative permutation sending HOLD,” “the predicate equals nmcover
axis-cover HOLD,” “the predicate equals nm2axz axis-cover HOLD,” “the
predicate equals nm2ax12z 1-in 2-out split HOLD,” “the predicate equals
the 1-axis opposite two-site seed,” “the predicate equals nmunopp union,”
“bits are Admissibility,” “split fail is UNDEFINED,” or “empty `O_i` is
UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each square vertex's own earliest
incoming set and own outgoing dual from the record prefix at that vertex's
`t+1`, reports split of the pair, reports the cyclic frame
`F=(m,o_next,o_prev)` as nm2cycfrmhol, reports Orient as nm2oricyclz
lex-largest cyclic, reports `P` on each formed six-neighbor edge of the
reverse yz square `A-D-B-E` at `x=0` and of the face yz square
`C-C1-C2-C3` at `x=1`, reports the holonomy products, reports distance-2 read
of those squares from formed graph-distance-2 translates, lists new records
in `B_3(0)` between `t` and `t+1` that meet a vertex's six-neighbors, and
checks Theorems 1--3. It also
checks that reverse distance-2 read fails and face distance-2 read fails, that
holonomy of the reverse square fails and holonomy of the face square
fails, that a vertex outside `B_3(0)` is fail not `UNDEFINED`, that
nm2yzrdn2 reverse fails after holonomy HOLDs on the opposite seed, that
nm2yzrdsl neighbor-read reverse fails at graph distance 1 on this seed, that
nm2holyzrd reverse HOLDs on the opposite seed, that nm2holyz holonomy
reverse HOLDs and holonomy face fails from the product at `S` alone, that
nm2rdholfz neighbor-read of xy holonomy reverse fails and face fails, that
a mutation ignoring holonomy at `S` would HOLD reverse from the `−e_3`
translate, that nm2cycfrmz transport reverse fails and transport face
HOLDs while holonomy face fails, that scalar neighbor-read reverse fails,
that unique nonnegative permutation sending fails at each of `A,B,C,D`,
that leftover-axis face fails because C
and D swap `(m,pair)` columns and lex-one reverse fails from `e1<e2<e3`
order independent of `m`, that split fail is holonomy fail not
`UNDEFINED`, that empty `O_next` or empty `O_prev` is Orient fail not
`UNDEFINED`, that the 1-axis opposite two-site seed is a different member
with `t(A)=1`, that #7477 same-lock is a different member with `t(A)=1`,
that LIVE three-axis as a three-site seed is a different member with
reverse holonomy fail, that leftover-empty fail is a different predicate,
that leftover of `M` alone and leftover of `O` alone are different objects,
that mixed sets remain sets, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
that the second pair is a new seed not a formed child, that the y-probes
and x-probes of this seed are not this letter, and that the display is not
the two-tick lock-count clock composition. No runner cache is written.
