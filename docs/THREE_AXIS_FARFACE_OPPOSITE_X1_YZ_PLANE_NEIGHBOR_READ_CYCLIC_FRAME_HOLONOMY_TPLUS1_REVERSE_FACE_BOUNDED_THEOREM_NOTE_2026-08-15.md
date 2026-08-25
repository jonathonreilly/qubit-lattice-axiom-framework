---
claim_id: three_axis_farface_opposite_x1_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of x=1 yz-plane cyclic-frame holonomy at t+1 on the three-axis far-face opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_farface_opposite_x1_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of X=1 Yz-Plane Cyclic-Frame Holonomy At t+1 Reverse And Face On The Three-Axis Far-Face Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of cyclic-frame holonomy around the x=1 yz unit
square of simultaneous earliest incoming set `M` and outgoing dual `O` at
each vertex's `τ=t+1`, and reverse/face from that neighbor-read, on the
three-axis far-face opposite seed in `B_3(0)={n:n·n<=9}`. `F` and Orient as
nm2holyz. Squares as nm2holyz2x. Holonomy as nm2holyz2x. Neighbor-read as
nm2holyzrd on those squares. Reverse yz square at `x=1`: `A=(1,0,0)`,
`D=(1,1,0)`, `B=(1,1,1)`, `E=(1,0,1)`. Face yz square at `x=2`:
`C=(2,0,0)`, `C1=(2,1,0)`, `C2=(2,1,1)`, `C3=(2,0,1)` that lie in
`B_3(0)`. Do not score the x=0 square (that is nm2holyz). Drop any vertex
outside `B_3(0)` as fail, not `UNDEFINED`. Let
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
product is the 3×3 identity. Neighbor-read HOLDs at a square `S` if and
only if holonomy(`S`) HOLDs and some formed 6-NN translate of `S` (shift
by one lattice unit in `B_3(0)`) has holonomy HOLD. If holonomy fails at
`S`, neighbor-read fails, not `UNDEFINED`. Reverse HOLDs if and only if
neighbor-read of the `x=1` yz square `A-D-B-E` HOLDs. Face HOLDs if and
only if neighbor-read of the `x=2` yz square `C-C1-C2-C3` HOLDs. Face is
displayed, not adopted. Cover and split do not score handedness. This is
not leftover of nm2holyz2x two-axis x=1 yz-square holonomy reverse fail
face fail: those two-axis holonomy bits match this reverse fail and this
face fail, but nm2holyz2x scores the product at `S` alone on the two-axis
seed from singleton `M={−e_3}` at `A,D`. This is not leftover of
nm2holyz2n two-axis neighbor-read of x=1 yz holonomy reverse fail face
fail: that reverse also fails because holonomy at `S` fails, but there
the `−e_1` translate is the x=0 square whose holonomy HOLDs; here that
same translate fails because the third pair makes the x=0 square fail.
This is not leftover of nm2holyz2xf far-face x=1 yz-square holonomy
reverse fail face fail: those holonomy bits match this reverse fail and
this face fail, but nm2holyz2xf scores the product at `S` alone. This is
not leftover of nm2holyzrd neighbor-read of x=0 yz holonomy reverse HOLD
face fail: that reverse HOLDs on the x=0 square, while this reverse is
the x=1 square. This is not leftover of nm2yzrdfz far-face neighbor-read
of x=0 yz holonomy reverse fail face fail: that reverse is the x=0
square. This is not leftover of nm2holyzfz far-face yz-square holonomy
reverse fail face fail: that reverse is the `x=0` square and fails from
split fail at origin, while this reverse is the `x=1` square. This is
not leftover of nm2holyz cyclic-frame holonomy reverse HOLD on the `x=0`
yz square and face fail on the `x=1` yz square: those bits are two-axis;
this display takes the `x=1` square as reverse and the parallel `x=2`
square as face on the three-axis far-face seed. Reverse here fails because
`A=(1,0,0)` and `D=(1,1,0)` are 2-in mixed `M={±e_3}` so unique `m`
fails, not because a singleton `m=−e_3` misses a cyclic outgoing slot as
in nm2holyz2x. Face here fails because
`C2=(2,1,1)` and `C3=(2,0,1)` are split fail from mixed two-axis `M` and
empty `O`, not because a cyclic slot is empty. This is not leftover of
nm2cycfrmhol cyclic-frame holonomy
reverse HOLD face fail on the xy-plane square `A-D-B-E` at `z=1`: that
product is the identity and that face fails because `C1,C2` at `z=2` are
2-in split fail, but those vertices are not this x=1 yz square. This is
not leftover of nm2cycfrmz cyclic-frame transport reverse HOLD face HOLD:
transport is existential at a vertex, holonomy is the product around a
square. Transport face HOLDs on the z-probes while holonomy face of this
yz square fails. This is not leftover of nm2oricyclz cyclic Orient reverse
HOLD whose bits are equal `±1` signs, not a four-edge product. This is not
leftover of scalar neighbor-read of Orient. This is not leftover of a
unique nonnegative permutation sending. This is not leftover of nm2orichz
leftover-axis reverse HOLD whose face fails because C and D swap
`(m,pair)` columns: those signs are not the holonomy product, and
holonomy face fails from split fail at `C,C1`. This is not leftover of
nm2orionez lex-one reverse fail whose face HOLDs from `e1<e2<e3` order
independent of `m`. This is not leftover of nm2chiralz lexicographic
unsigned `o1,o2` orientation. This is not leftover of nm2oridetz unique
signed outgoing letters. This is not leftover of nm2axz axis-cover. This
is not leftover of nm2ax12z 1-in 2-out split. This is not leftover of
leftover-of-`M` alone. This is not leftover of leftover-of-`O` alone. This
is not leftover-empty fail of leftover axis. This is not leftover of
nmunopp union. This is not leftover of nmt2opp `M` frozen at `t`. This is
not leftover of nmot2opp two-tick composition. This is not leftover of
nmoutopp untimed eventual-`O`. This is not leftover of mixed #7188
fail/fail. This is not leftover of the 1-axis opposite two-site seed.
This is not leftover of the same-lock two-site seed. This is not leftover
of the two-axis opposite seed of nm2holyz2x. This is not leftover of the
near-face three-axis seed. The second pair is a
new seed, not a formed child. The third pair is a new seed, not a formed
child. Uniqueness is not required. Mixed remains a
set. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_farface_opposite_x1_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_farface_opposite_x1_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py)

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
edge matrices around the square. Neighbor-read of that holonomy HOLDs at a
square if and only if the square's holonomy HOLDs and some formed 6-NN
translate in `B_3(0)` also has holonomy HOLD. Reverse and face are scored
on neighbor-read HOLD of the reverse square and of the face square.
Holonomy of nm2holyz2x is a different readout: it scores the product at
`S` alone on the two-axis seed. Neighbor-read of x=1 yz holonomy on that
two-axis seed is a different readout: there the `−e_1` translate HOLDs
while holonomy at `S` fails. Holonomy of nm2holyz2xf is a different
readout: it scores the product at `S` alone on this far-face seed.
Neighbor-read of x=0 yz holonomy on the two-axis seed is a different
readout and HOLDs reverse while this reverse fails. Neighbor-read of x=0
yz holonomy on this far-face seed is a different readout and fails
reverse on the x=0 square. Transport of nm2cycfrmz
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
claim_type_reason: "Exact report of neighbor-read of cyclic-frame holonomy around the x=1 yz unit square of M and O at t+1 on the three-axis far-face opposite seed, F and Orient at the eight square vertices, P on each edge, holonomy matrices, neighbor-read of those squares, reverse fail and face fail from neighbor-read of the x=1 and x=2 yz squares; uniqueness of a sending is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_farface_opposite_x1_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face
target_blocker_text: "display neighbor-read of x=1 yz-plane cyclic-frame holonomy reverse/face on the three-axis far-face opposite seed with x=2 as face, not nm2holyz2x two-axis x=1 yz-square holonomy, not nm2holyz2n two-axis neighbor-read of x=1 yz holonomy, not nm2holyz2xf far-face x=1 yz-square holonomy, not nm2holyzfz far-face yz-square holonomy, not nm2holyzrd neighbor-read of x=0 yz holonomy, not nm2yzrdfz far-face neighbor-read of x=0 yz holonomy, not nm2holyz x=0 reverse HOLD, not nm2cycfrmhol xy-square holonomy, not nm2cycfrmz transport, not scalar neighbor-read of Orient, not unique nonnegative sending, not leftover-axis, not lex-one e1<e2<e3, not unique |O_i|=1, not unsigned axis units, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of cyclic-frame holonomy of F around the x=1 yz unit square at t+1 displayed; do not score the x=0 square, do not write holonomy into Admissibility, do not reduce to nm2holyz2x two-axis x=1 yz-square holonomy, do not reduce to nm2holyz2n two-axis neighbor-read of x=1 yz holonomy, do not reduce to nm2holyz2xf far-face x=1 yz-square holonomy, do not reduce to nm2holyzfz far-face yz-square holonomy, do not reduce to nm2holyzrd neighbor-read of x=0 yz holonomy, do not reduce to nm2yzrdfz far-face neighbor-read of x=0 yz holonomy, do not reduce to nm2holyz x=0 reverse HOLD, do not reduce to nm2cycfrmhol xy-square holonomy, do not reduce to nm2cycfrmz transport, do not reduce to scalar neighbor-read of Orient, do not reduce to unique nonnegative permutation sending, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-smallest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace holonomy by unique outgoing letters, do not replace holonomy by existential opposite of signed locks, do not replace holonomy by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of cyclic-frame holonomy around the x=1 yz unit square of M and O at t+1 on the three-axis far-face opposite seed and reverse/face from that neighbor-read; displayed, not adopted"
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

No larger host is used. The reverse yz-plane unit square at `x=1` and the parallel face
square at `x=2` are the only cycles whose neighbor-read of cyclic-frame
holonomy of `F=(m,o_next,o_prev)` of `M` and `O` is scored:

```text
A = (1,0,0),  D = (1,1,0),  B = (1,1,1),  E = (1,0,1).
C = (2,0,0),  C1 = (2,1,0),  C2 = (2,1,1),  C3 = (2,0,1).
```

A vertex outside `B_3(0)` is fail, not `UNDEFINED`. Do not score the x=0 square.
These are not the x=0 yz square `origin`, `(0,1,0)`, `(0,1,1)`,
`(0,0,1)` of nm2holyz. These are not the xy-plane square `A=(0,0,1)`,
`D=(1,0,1)`, `B=(1,1,1)`, `E=(0,1,1)` of nm2cycfrmhol. These are not the
y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`. These are
not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`. Same
process as nm2axz. `F` and Orient as nm2holyz. All four reverse vertices
lie in `B_3(0)`. All four face vertices lie in `B_3(0)`. The parallel
yz square at `x=3` has `(3,1,0)` outside `B_3(0)` and is holonomy fail,
not `UNDEFINED`.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. Site `(0,0,−1)` locks `+e_3`. Site
`(0,1,−1)` locks `−e_3`. The second pair is a new seed, not a formed
child of the first pair. The third pair is a new seed, not a formed
child. This seed is not the two-axis opposite seed of nm2holyz2x. This
seed is not the near-face three-axis seed with third pair at `(2,0,0)`
and `(2,1,0)`. This seed is not the 1-axis opposite two-site seed
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
Neighbor-read HOLDs at a square S iff holonomy(S) HOLDs and some
formed 6-NN translate of S (shift by one lattice unit in B_3(0))
has holonomy HOLD.
If holonomy fails at S, neighbor-read fails, not UNDEFINED.
Uniqueness of a sending neighbor is not required.
Uniqueness of a holonomy-HOLDING translate is not required.
```

Neighbor-read of the scalar Orient sign HOLDs at `q` if and only if
`Orient(q)` is `±1` and some formed six-neighbor has the same sign. That
is a different object. Transport of nm2cycfrmz HOLDs at `q` if and only if
some formed six-neighbor hosts a signed-permutation sending. That is a
different object: transport HOLDs at the four reverse yz vertices, so
transport reverse HOLDs, while transport fails at `C` and at `C1` of the
`x=1` reverse square. Holonomy of nm2holyz2x reverse fails because `A`
and `D` are split fail from singleton `M={−e_3}`. Holonomy of nm2holyz2xf
reverse fails because `A` and `D` are split fail from mixed `M={±e_3}`.
Holonomy face fails because `C2` and `C3` are
split fail. Those holonomy bits match this reverse fail and this face
fail, but they are not this neighbor-read: a mutation that scored only a
holonomy-HOLDING 6-NN translate, ignoring holonomy at `S`, fails reverse
here because every formed 6-NN translate of the reverse square has
holonomy fail, including the `−e_1` translate which is the x=0 square.
Neighbor-read of x=0 yz holonomy on the two-axis seed HOLDs reverse and
fails face. Neighbor-read of x=0 yz holonomy on this far-face seed fails
reverse. A unique nonnegative
permutation sending is a different object and fails at each reverse
vertex. Transport of nm2cycfrmz on the z-probes reverse HOLDs and face
HOLDs, leftover of that transport, not this yz-square neighbor-read.

Reverse neighbor-read cyclic-frame holonomy holds if and only if
neighbor-read of the `x=1` yz square `A-D-B-E` HOLDs. Face neighbor-read
cyclic-frame holonomy holds if and only if neighbor-read of the `x=2` yz
square `C-C1-C2-C3` HOLDs. If holonomy of a square fails, neighbor-read
of that square fails, not `UNDEFINED`.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse and face on the z-probes
without reading cyclic signed columns; cover of the x=1 reverse pair
`A,D` fails as this reverse fails, from a different object; cover of the
x=2 face pair `C,C1` HOLDs while this face fails. Identifying split
reverse with this reverse is refused: split HOLDs reverse and face on the
z-probes without the four-edge product; split face HOLDs on `C,C1` of
the `x=2` square while holonomy face fails at `C2,C3`. Identifying
leftover-empty fail with this reverse is refused: leftover-empty fail
scores empty leftover as reverse fail and face fail on the z-probes,
while leftover of the union at reverse `A,D` is `{e_2}` so leftover
reverse HOLDs while this reverse fails; leftover face-far HOLDs at
`C2,C3` while this face fails. Identifying nm2holyz2x two-axis x=1 yz-square holonomy with this reverse is refused:
nm2holyz2x reverse fails and face fails from the product at `S` alone
from singleton `M={−e_3}` at `A,D`. Identifying nm2holyz2n two-axis
neighbor-read of x=1 yz holonomy with this reverse is refused: that
reverse fails even though `holonomy(A-D-B-E − e_1)` HOLDs on the
two-axis seed. Identifying nm2holyz2xf far-face x=1 yz-square holonomy
with this reverse is refused: nm2holyz2xf reverse fails and face fails
from the product at `S` alone on this seed. Identifying nm2holyzrd neighbor-read of x=0 yz
holonomy with this reverse is refused: that reverse HOLDs and that face
fails. Identifying nm2yzrdfz far-face neighbor-read of x=0 yz holonomy
with this reverse is refused: that reverse fails on the x=0 square.
Identifying nm2holyzfz far-face yz-square holonomy with this reverse is
refused: that reverse fails on the x=0 square from split fail at origin.
Identifying nm2holyz x=0 yz holonomy with
this reverse is refused: that reverse HOLDs and that face fails on the
x=0 and x=1 squares; this reverse is the previous face square. Identifying
nm2cycfrmhol xy-square holonomy with this reverse is refused: that reverse
HOLDs and that face fails on different vertices. Identifying nm2cycfrmz
transport with this reverse is refused: transport reverse HOLDs and
transport face HOLDs on the z-probes, while this reverse fails and this
face fails. Identifying lexicographic unsigned `o1,o2` with this reverse
is refused: unsigned reverse fails as this reverse fails, from a different
object; unsigned face HOLDs while this face fails. Identifying nm2orionez
lex-one signed `e1<e2<e3` with this reverse is refused: lex-one reverse
fails from axis order independent of `m`; lex-one face HOLDs while this
face fails. Identifying unique signed `|O_i|=1` with this reverse is
refused: unique signed reverse fails as this reverse fails, from a
different object. Identifying leftover-axis orientation with this reverse
is refused: leftover-axis reverse HOLDs and face fails because C and D
swap `(m,pair)` columns; those two signs are not the holonomy product of
four edge sendings, and holonomy reverse fails from split fail at `A,D`.
Identifying cyclic lex-smallest with this reverse is refused:
lex-smallest picks `+e` if both signs. Identifying a named sign of those
locks with reverse or face is refused: named-sign lettering lost the axis.

## Theorem 1 — ticks, `F`, Orient, `P` on each edge, holonomy, neighbor-read

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
`e1<e2<e3` order independent of `m`. This display reads neighbor-read of the cyclic-frame
holonomy of `(m,o_next,o_prev)` around the two yz-plane unit squares of
those same timed sets:

```text
t(A)=2
t(D)=2
t(B)=1
t(E)=1
t(C)=3
t(C1)=3
t(C2)=4
t(C3)=4
M(A, τ) = {+e_3, −e_3}
M(B, τ) = {+e_1}
M(C, τ) = {+e_1}
M(D, τ) = {+e_3, −e_3}
M(E, τ) = {+e_1}
M(C1, τ) = {+e_1}
M(C2, τ) = {−e_2, +e_3, −e_3}
M(C3, τ) = {+e_2, +e_3, −e_3}
O(A, τ) = {+e_1}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {−e_2, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
O(E, τ) = {−e_2, +e_3, −e_3}
O(C1, τ) = {+e_2, +e_3, −e_3}
O(C2, τ) = {}
O(C3, τ) = {}
split(A) = fail
split(B) = hold
split(C) = hold
split(D) = fail
split(E) = hold
split(C1) = hold
split(C2) = fail
split(C3) = fail
Orient(A) = fail
m(B) = +e_1
i(B) = 1
o_next(B) = +e_2
o_prev(B) = −e_3
det(B) = -1
Orient(B) = −1
Orient(D) = fail
m(E) = +e_1
i(E) = 1
o_next(E) = −e_2
o_prev(E) = −e_3
det(E) = 1
Orient(E) = +1
m(C) = +e_1
i(C) = 1
o_next(C) = −e_2
o_prev(C) = −e_3
det(C) = 1
Orient(C) = +1
m(C1) = +e_1
i(C1) = 1
o_next(C1) = +e_2
o_prev(C1) = −e_3
det(C1) = -1
Orient(C1) = −1
Orient(C2) = fail
Orient(C3) = fail
F(A) = fail
F(B) = (+e_1, +e_2, −e_3)
F(C) = (+e_1, −e_2, −e_3)
F(D) = fail
F(E) = (+e_1, −e_2, −e_3)
F(C1) = (+e_1, +e_2, −e_3)
F(C2) = fail
F(C3) = fail
P(A→D) = fail
P(D→B) = fail
P(B→E) = [1 0 0; 0 -1 0; 0 0 1]
P(E→A) = fail
holonomy(A-D-B-E) = fail
P(C→C1) = [1 0 0; 0 -1 0; 0 0 1]
P(C1→C2) = fail
P(C2→C3) = fail
P(C3→C) = fail
holonomy(C-C1-C2-C3) = fail
neighbor-read(A-D-B-E) = fail
neighbor-read(C-C1-C2-C3) = fail
holonomy(A-D-B-E − e_1) = fail
```

`A=(1,0,0)` is not a seed: `t(A)=2` with mixed incoming `{+e_3,−e_3}`.
All four reverse vertices are formed children, not the four seeds of
nm2holyz. Mixed remains a set: `M(A,τ)` and `M(D,τ)` each have both
`±e_3`, `O(B,τ)` has three outgoing steps and `O(E,τ)` has three outgoing
steps, and `M(C2,τ)` has three incoming steps. Unique outgoing letters
would assign `UNDEFINED` at mixed `O`. Unique signed `|O_i|=1` fails at
`B` and at `E` because each has both `±e_3`. Lex-largest picks `−e` on
that mixed cyclic slot, so `(o_next,o_prev)` is defined at `B` and at `E`.
Split fails at `A` and at `D` because `Axis(M)={e_3}` and `Axis(O)` miss
`e_2`, so cover fails, and unique `m` fails from mixed `{±e_3}`. Orient
fails, not `UNDEFINED`. This is leftover of nm2holyz2x only as the same
fail bit: that two-axis reverse has singleton `M={−e_3}` at `A` and at
`D` and empty `O_prev`; the third pair here supplies `+e_3` into those
same vertices. At `C2` and at `C3`, `M` occupies two axes and `O` is
empty, so split fails, not `UNDEFINED`. Cover HOLDs at `C` and at `C1` of
the `x=2` face and does not score that holonomy fails at `C2,C3`. O is not
M.

On the 1-axis opposite two-site seed, `t(A)=3` and this reverse square is
not four seeds. That is leftover of the first pair. Here both `(0,0,1)`
and `(0,1,1)` are seeds of a second opposite pair on a second axis, and
origin and `(0,1,0)` are the first pair, and `(0,0,−1)` and `(0,1,−1)` are
the third pair. On nm2holyz the `x=0` yz square is exactly the first two
pairs and reverse HOLDs; this display does not score that square, and on
this far-face seed that `x=0` square fails. On nm2holyz2x the two-axis
x=1 reverse fails from singleton `M={−e_3}`; leftover of that two-axis
x=1 fail, not this mixed `{±e_3}`. On nm2holyz2n the two-axis neighbor-read
of that x=1 reverse fails even though the `−e_1` translate HOLDs. On
nm2holyz2xf the far-face x=1 reverse fails from mixed `{±e_3}` as the
product at `S` alone. On nm2holyzfz the far-face `x=0` reverse fails from
split fail at origin; leftover of that far-face `x=0` fail, not this `x=1`
square. On the xy-plane square of nm2cycfrmhol, reverse HOLDs
and face fails from 2-in split fail at height 2; those vertices are not
this x=1 yz square. On the y-probes of this same seed, y-probe reverse
fails as this reverse fails, from a different object.

New records in `B_3(0)` between `t` and `t+1` that meet a vertex's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at `A`, `B`, `E`,
`C`, and `C1`; at `D`, `O` at `t` is `{−e_1}` and at `t+1` is `{±e_1}`.
At `t`, split fails at each reverse vertex, Orient is fail, not
UNDEFINED, and the cyclic frame fails, not UNDEFINED. Transport at `t`
therefore fails, not UNDEFINED.

`B` and `E` each have a formed six-neighbor with split HOLD and a signed
permutation sending. Uniqueness of that neighbor is not required. First
witness in six-neighbor order: `B` sends to `(0,1,1)`; `E` sends to
`(0,0,1)`. `A` and `D` are split fail, so they have no sending. Those
existential transport bits at `B` and `E` are leftover of nm2cycfrmz
cyclic-frame transport, not this neighbor-read. Reverse-square holonomy
fails because `A` and `D` are split fail, so neighbor-read of that square
fails, not `UNDEFINED`. Face-square holonomy fails because `C2` and `C3`
are split fail from mixed two-axis `M` and empty `O`, so neighbor-read of
that square fails. The `−e_1` translate of the reverse square is the x=0
yz square whose holonomy fails on this far-face seed; every formed 6-NN
translate of the reverse square has holonomy fail. The
3-split is a field: opposite Orient at a neighbor is allowed when
`det(P)` equals the product of the two signs. This is not leftover of
nm2holyz2x: that reverse fails and that face fails from the product at
`S` alone from singleton `M={−e_3}`. This is not leftover of nm2holyz2n:
that reverse fails even though the `−e_1` translate HOLDs. This is not
leftover of nm2holyz2xf: that reverse fails from the product at `S`
alone on this seed. This is not leftover of nm2holyzrd: that reverse HOLDs
on `x=0`. This is not leftover of nm2yzrdfz: that reverse fails on `x=0`.
This is not leftover of nm2holyzfz: that reverse fails on `x=0` from
split fail at origin. This is not leftover of nm2holyz: that reverse HOLDs
on `x=0` and that face fails at `x=1` missing cyclic slots, while this
reverse fails at those same `x=1` vertices from mixed `{±e_3}` and this
face fails at `x=2` mixed `M`. This is not leftover of nm2cycfrmhol: that
face fails at `z=2` 2-in vertices.

## Theorem 2 — reverse from neighbor-read of cyclic-frame holonomy at `τ`

Reverse neighbor-read cyclic-frame holonomy holds if and only if
neighbor-read of the `x=1` yz square `A-D-B-E` HOLDs. Split fails at `A`
and at `D` because mixed `M={±e_3}` makes unique `m` fail and cover miss
`e_2`, so `P(A→D)`, `P(D→B)`, and `P(E→A)` fail. Holonomy of the reverse
square fails, so neighbor-read fails, not `UNDEFINED`. This is fail of
that neighbor-read, not leftover of nm2holyz2x two-axis x=1 yz-square
holonomy, not leftover of nm2holyz2n two-axis neighbor-read of x=1 yz
holonomy, not leftover of nm2holyz2xf far-face x=1 yz-square holonomy,
not leftover of nm2holyzfz far-face yz-square holonomy, not leftover of
nm2holyzrd neighbor-read of x=0 yz holonomy, not leftover of nm2yzrdfz
far-face neighbor-read of x=0 yz holonomy, not leftover of nm2holyz
x=0 reverse HOLD, not leftover of nm2cycfrmhol xy-square holonomy, not
leftover of nm2cycfrmz cyclic-frame transport, not leftover of
nm2oricyclz cyclic Orient equal signs, not leftover of scalar
neighbor-read, not leftover of a unique nonnegative permutation sending,
not leftover of nm2chiralz lexicographic unsigned `o1,o2`, not leftover of
nm2oridetz unique signed outgoing letters, not leftover of nm2orichz
leftover-axis, not leftover of nm2orionez lex-one, not leftover of nm2axz
axis-cover, not leftover of nm2ax12z 1-in 2-out split, not leftover-empty
fail, and not exist-opposite.

Reverse neighbor-read cyclic-frame holonomy at τ: fail

Both squares are defined, so this is not `UNDEFINED`. Cover reverse of
the x=1 square fails because cover fails at `A` and at `D`. Split reverse
of that pair fails. Cover and split do not score handedness. Leftover of
the union at `A` and at `D` is `{e_2}` and `{e_2}`, so leftover reverse
HOLDs while this reverse fails. Leftover of `M` at `A` and at `D` is
`{e_1,e_2}` on both, so leftover of `M` reverse HOLDs while this reverse
fails. Leftover of `O` at `A` is `{e_2,e_3}` and at `D` is `{e_2,e_3}`,
so leftover of `O` reverse HOLDs while this reverse fails.
Exist-opposite reverse of signed `M` at `A,D` HOLDs from mixed `{±e_3}`
on both vertices, while this reverse fails. Exist-opposite reverse of
signed `O` at `A,D` HOLDs. nm2holyz2x reverse fails from the product at
`S` alone from singleton `M={−e_3}`; this reverse is neighbor-read of
that same square on the far-face seed, and it fails because holonomy at
`S` fails and `holonomy(A-D-B-E − e_1)` fails. nm2holyz2n reverse fails
on the two-axis seed even though that `−e_1` translate HOLDs.
nm2holyz2xf reverse fails from the product at `S` alone on this seed.
nm2holyzrd reverse HOLDs on the x=0 square; this reverse is not that
square. nm2yzrdfz reverse fails on the x=0 square. nm2holyz reverse
HOLDs because the product around the x=0 square is the identity on the
two-axis seed; on this far-face seed that x=0 square fails, and this
reverse is not that square. nm2holyzfz reverse fails on the `x=0` square
from split fail at origin. nm2cycfrmz transport reverse HOLDs on the z-probes because
transport HOLDs at those `A` and `B`; that is existential at two
vertices, not the four-edge product. Leftover-axis reverse HOLDs with
`−1,−1` bits on the z-probes, but leftover-axis is two signs, not
`P12 P23 P34 P41`. Those leftovers are not this display.

Reverse fails.

## Theorem 3 — face from neighbor-read of cyclic-frame holonomy at `τ`

Face neighbor-read cyclic-frame holonomy holds if and only if
neighbor-read of the `x=2` yz square `C-C1-C2-C3` HOLDs. Split HOLDs at
`C` and at `C1`, and `P(C→C1)` is a signed permutation, but split fails
at `C2` and at `C3` because `M` occupies two axes and `O` is empty, so
`P(C1→C2)`, `P(C2→C3)`, and `P(C3→C)` fail. Holonomy of the face square
fails, so neighbor-read fails, not `UNDEFINED`. Displayed, not adopted.

Face neighbor-read cyclic-frame holonomy at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face HOLDs at `C` and at `C1` of the `x=2` square because cover
HOLDs there. Split face HOLDs at that pair. Cover and split do not score
handedness, and they do not read `C2,C3`. Transport face HOLDs at `C` and
at `C1` and fails at `C2,C3`. Leftover of the union at `C2` and at `C3`
is `{e_1}` and `{e_1}`, so leftover face-far HOLDs while this face fails.
Leftover of the union at `C` and at `C1` is empty, so leftover-empty fail
on that pair is fail as this face fails, from a different object.
nm2cycfrmz transport face HOLDs on the z-probes; that existential pair is
not this neighbor-read. nm2holyz2x face fails at `x=2` from mixed two-axis
`M` on the product at `S` alone on the two-axis seed; this face is
neighbor-read of that same square on the far-face seed. nm2holyz2xf face
fails at `x=2` from the product at `S` alone. nm2holyz face fails at `x=1`
from empty cyclic slots at those `C,C1`; this face fails at `x=2` from
mixed two-axis `M`. On the 1-axis
opposite two-site seed, reverse neighbor-read of this x=1 yz square fails
and face neighbor-read fails; here `t(A)=2` and face holonomy fails at
`C2,C3`. The four y-probes of this same seed give cyclic Orient `+1` at
y-probe `A` and Orient fail at y-probe `D` from split fail, so oriented
y-face fails. The four x-probes give oriented reverse fail and oriented
face fail. Those probe-direction readouts are not this x=1 yz-plane
neighbor-read. Exist-opposite face of signed `M` at `C,C1` fails.
Exist-opposite face of signed `O` at `C,C1` HOLDs while this face fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Leftover of the union at reverse `A` and reverse `D` is
`{e_2}`, nonempty, so leftover reverse HOLDs while this reverse fails.
Cover fails at reverse `A` and at reverse `D`. Split fails at reverse
`A` and at reverse `D`. Orient at reverse `A` and at reverse `D` is fail
from mixed `M={±e_3}` so unique `m` fails. A vertex outside `B_3(0)`, for example the parallel yz square
at `x=4`, is holonomy fail, not `UNDEFINED`. The parallel yz square at
`x=3` has `(3,1,0)` outside `B_3(0)` and is holonomy fail, not
`UNDEFINED`.

Face fails.

## What this note does not claim

- It does not replace neighbor-read by nm2holyz2x two-axis x=1 yz-square holonomy.
- This is not leftover of nm2holyz2x two-axis x=1 yz-square holonomy.
- It does not replace neighbor-read by nm2holyz2n two-axis neighbor-read of x=1 yz holonomy.
- This is not leftover of nm2holyz2n two-axis neighbor-read of x=1 yz holonomy.
- It does not replace neighbor-read by nm2holyz2xf far-face x=1 yz-square holonomy.
- This is not leftover of nm2holyz2xf far-face x=1 yz-square holonomy.
- It does not replace neighbor-read by nm2holyzfz far-face yz-square holonomy.
- This is not leftover of nm2holyzfz far-face yz-square holonomy.
- It does not replace neighbor-read by nm2holyzrd neighbor-read of x=0 yz holonomy.
- This is not leftover of nm2holyzrd neighbor-read of x=0 yz holonomy.
- It does not replace neighbor-read by nm2yzrdfz far-face neighbor-read of x=0 yz holonomy.
- This is not leftover of nm2yzrdfz far-face neighbor-read of x=0 yz holonomy.
- It does not replace holonomy by nm2holyz x=0 reverse HOLD face fail.
- This is not leftover of nm2holyz x=0 reverse HOLD.
- It does not replace holonomy by nm2cycfrmz cyclic-frame transport.
- It does not replace holonomy by neighbor-read of the scalar Orient sign.
- It does not replace holonomy by a unique nonnegative permutation sending.
- It does not require a unique formed six-neighbor witness.
- It does not reprint nm2oricyclz cyclic Orient reverse hold face hold as this neighbor-read.
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
Admissibility. The three-axis far-face opposite seed process, cyclic-frame holonomy of
`(m,o_next,o_prev)` of `M` and `O` at `t+1` around the unit square, and the
reverse/face bits from that holonomy are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three-axis far-face opposite seed `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3` |
| ticks `t(A)`, `t(D)`, `t(B)`, `t(E)`, `t(C)`, `t(C1)`, `t(C2)`, `t(C3)` | Theorem 1; `2`, `2`, `1`, `1`, `3`, `3`, `4`, `4` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual at `B,E,C,C1`; empty at `C2,C3` |
| split at `τ` | Theorem 1; HOLD at `B,E,C,C1`; fail at `A,D,C2,C3` |
| unique signed `m`, axis index `i`, cyclic `(o_next,o_prev)` | Theorem 1; singleton `M` at `B,E,C,C1`; mixed `M` at `A,D,C2,C3` |
| integer `det(m,o_next,o_prev)` | Theorem 1; at `B,E` `-1`, `1`; at `C,C1` `1`, `-1` |
| Orient at `τ` | Theorem 1; reverse fail, fail, `−1`, `+1`; face `+1`, `−1`, fail, fail |
| cyclic frame `F=(m,o_next,o_prev)` | Theorem 1; fail at `A,D,C2,C3`; LIVE three-axis at `B,E,C,C1` |
| `P` on each reverse edge | Theorem 1; fail, fail, signed permutation, fail |
| holonomy matrix of `A-D-B-E` | Theorem 1; fail |
| holonomy matrix of `C-C1-C2-C3` | Theorem 1; fail |
| leftover of nm2holyz x=0 reverse HOLD | Theorem 2; x=0 square not scored; this reverse fails |
| leftover of nm2holyz2x two-axis x=1 yz-square holonomy | Theorem 2; two-axis singleton `M={−e_3}` at `A,D`; not this mixed `{±e_3}` |
| leftover of nm2holyz2n two-axis neighbor-read of x=1 yz holonomy | Theorem 2; two-axis `−e_1` translate HOLDs; this far-face translate fails |
| leftover of nm2holyz2xf far-face x=1 yz-square holonomy | Theorem 2; product at `S` alone; this reverse is neighbor-read |
| leftover of nm2holyzfz far-face yz-square holonomy | Theorem 2; x=0 reverse fail from split fail at origin; not this x=1 square |
| leftover of nm2holyzrd neighbor-read of x=0 yz holonomy | Theorem 2; that reverse HOLDs on x=0; this reverse is x=1 |
| leftover of nm2yzrdfz far-face neighbor-read of x=0 yz holonomy | Theorem 2; that reverse fails on x=0; this reverse is x=1 |
| leftover of nm2cycfrmz cyclic-frame transport | Theorem 1; transport reverse hold and transport face hold; not this letter |
| reverse from neighbor-read of cyclic-frame holonomy at `τ` | Theorem 2; `fail` |
| face from neighbor-read of cyclic-frame holonomy at `τ` | Theorem 3; `fail` |
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
| leftover of nm2oricyclz cyclic Orient equal signs | not this neighbor-read |
| leftover of nm2holyz2x two-axis x=1 yz-square holonomy | not this neighbor-read; product at S alone on the two-axis seed |
| leftover of nm2holyz2n two-axis neighbor-read of x=1 yz holonomy | not this reverse; two-axis `−e_1` translate HOLDs |
| leftover of nm2holyz2xf far-face x=1 yz-square holonomy | not this neighbor-read; product at S alone on this seed |
| leftover of nm2holyzfz far-face yz-square holonomy | not this reverse; x=0 square not scored |
| leftover of nm2holyzrd neighbor-read of x=0 yz holonomy | not this reverse; x=0 square not scored |
| leftover of nm2yzrdfz far-face neighbor-read of x=0 yz holonomy | not this reverse; x=0 square not scored |
| leftover of nm2holyz x=0 reverse HOLD | not this neighbor-read; x=0 square not scored |
| leftover of nm2cycfrmz cyclic-frame transport | not this neighbor-read |
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
| leftover of the same-lock two-site seed | not this display; #7477 same-lock face transport fails |
| leftover of the two-axis opposite seed of nm2holyz2x | not this display; third pair is a new seed |
| leftover of the near-face three-axis seed | not this display; third pair is at `(2,0,0)` and `(2,1,0)` |
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
| V1 | It answers the first-display question: neighbor-read of cyclic-frame holonomy around the x=1 yz unit square of `(m,o_next,o_prev)` of `M` and `O` at `t+1` on the three-axis far-face opposite seed, and reverse/face from the x=1 and x=2 squares. |
| V2 | Current main has no landed neighbor-read of cyclic-frame-holonomy reverse/face of timed `M` and `O` on the x=1 and x=2 yz-plane unit squares of the three-axis far-face opposite seed. |
| V3 | Edge sendings, two holonomy matrices, and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads neighbor-read of the four-edge signed-permutation product around a unit square at the same `t+1` cut, reverse fails and face fails while nm2holyz reverse HOLDs on x=0 on the two-axis seed and fails on this far-face seed, nm2holyz2n reverse fails while its `−e_1` translate HOLDs, nm2cycfrmz transport reverse HOLDs and transport face HOLDs, leftover reverse HOLDs at `A,D`, and nm2oricyclz Orient equality does not supply the product. |
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
| scalar neighbor-read of Orient | reuse equal Orient sign at some formed 6-NN | scalar HOLDs at z-probe `A` and fails at `B,C,D`; scalar reverse fails as this reverse fails, from a different object | ATTEMPTED |
| unique nonnegative permutation sending | require a unique sending with no minus signs | unique nonnegative sending fails at each of `A,B,C,D`; uniqueness is not required | ATTEMPTED |
| nm2holyz x=0 yz holonomy | reuse reverse HOLD on `x=0` and face fail on `x=1` | nm2holyz reverse HOLDs; this reverse is the previous face square and fails; this face is `x=2` mixed-`M` fail | ATTEMPTED |
| nm2cycfrmhol xy-plane holonomy | reuse holonomy reverse hold and face fail of `A-D-B-E` at `z=1` | that reverse HOLDs and that face fails on different vertices; this reverse is the `x=1` yz square of formed children; this face fails at `C2,C3` on `x=2` | ATTEMPTED |
| nm2cycfrmz cyclic-frame transport | reuse transport reverse hold and face hold from existential 6-NN sendings | transport reverse HOLDs and transport face HOLDs while this reverse fails and this face fails; transport is existential at a vertex, holonomy is the four-edge product | ATTEMPTED |
| nm2oricyclz cyclic Orient | reuse Orient reverse hold and face hold from equal `±1` signs | Orient reverse HOLDs and face HOLDs without a four-edge product; HOLDING cyclic #7451/#7452 is the frame sign, not holonomy | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face hold | unsigned reverse fails as this reverse fails, from unsigned columns; unsigned face HOLDs while this face fails | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed reverse fails as this reverse fails, from `|O_i|≠1`; an opposite pair in `O` makes `|O_i|≠1` but lex-largest still picks `−e` | ATTEMPTED |
| nm2orichz leftover-axis | reuse leftover-axis reverse hold and face fail | leftover-axis reverse HOLDs (`−1,−1`) while this reverse fails; leftover-axis face fails because C and D swap `(m,pair)` columns; holonomy face fails from split fail at `C2,C3`; those two signs are not `P12 P23 P34 P41` | ATTEMPTED |
| nm2orionez lex-one | reuse lex-one reverse fail and face hold | lex-one reverse fails from `e1<e2<e3` order independent of `m`; this reverse fails from split fail at `A,D`; lex-one face HOLDs while this face fails | ATTEMPTED |
| cyclic lex-smallest | reuse same cyclic axes with `+e` if both signs | lex-smallest reverse HOLDs with `+1,+1` and face HOLDs with `−1,−1`; this reverse fails and this face fails | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse hold and cover face hold on these z-probes | cover HOLDs reverse and face without cyclic signed columns; cover face HOLDs at `C,C1` while this face fails | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse split reverse hold and split face hold | split HOLDs reverse and face on z-probes `A,B,C,D` without the four-edge product; Cover and split do not score handedness; split face HOLDs at `C,C1` while this face fails | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse HOLDs at `A,D` while this reverse fails; leftover face-far HOLDs at `C2,C3` while this face fails | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at reverse `A` and `D` is `{e_1,e_2}` on both, so leftover of `M` reverse HOLDs while this reverse fails | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`, nonempty unequal | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `M` at `A,D` HOLDs from mixed `{±e_3}` while this reverse fails; exist-opposite reverse of signed `O` at `A,D` HOLDs while this reverse fails; exist-opposite face of signed `O` at `C,C1` HOLDs while this face fails | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence HOLDs at each of `A,B,C,D` without cyclic columns; pair-presence face HOLDs while this face fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-largest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is `−1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member both agree; flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient from `+1` to `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, Orient fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=2` and the reverse yz square is four formed children | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe reverse fails (`+1,−1`) and y-face fails; this letter is the yz-plane unit square | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the yz-plane unit square | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-largest outgoing determinant orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face fail on the x=1 and x=2 yz-plane unit squares | ATTEMPTED |
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
nmcover axis-cover, missing identification of Orient with nm2axz axis-cover,
missing identification of Orient with nm2ax12z 1-in 2-out split, missing
identification of this seed with the 1-axis opposite two-site seed, and
missing Record identification of Orient reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three disjoint opposite seed pairs `+e_1/−e_1`,
`+e_2/−e_2`, and `+e_3/−e_3`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
next/prev axes of `Axis(M)`, lex-largest signed outgoing letter under
`+e < −e` (hence `−e` if both signs), integer determinant sign, empty
`O_next` or empty `O_prev` as Orient fail not `UNDEFINED`, split fail as
Orient fail not `UNDEFINED`, four z-probes with seed `A`, second pair as a
new seed not a formed child, third pair as a new seed not a formed child,
and mixed remains a set are declared. No
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
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | edge sendings, two holonomy matrices, reverse/face from holonomy | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for cyclic-frame holonomy
reverse/face, a formation-rate rule, and a physical selector among 1-in
2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Holonomy reverse fail and face fail are only leftover of
nm2holyz face fail, or of mixed #7188 fail/fail, or of nm2cycfrmz
cyclic-frame transport, or of nm2oricyclz cyclic Orient equal signs, or
of neighbor-read of the scalar Orient sign, or of cover and split;
leftover-axis already answers reverse HOLD and face fail; leftover of
the union at `A,D` already answers reverse HOLD; unique signed `|O_i|=1`
already answers mixed `O`; leftover of `M` alone already answers reverse;
exist-opposite of signed `O` already answers reverse; the second pair is
only the formed child `(0,0,1)` of the 1-axis seed; unique outgoing
letters should be required; cyclic lex-smallest already gives HOLD bits
with opposite signs; and unsigned incoming axis already gives the same
signs because each `M` letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail on the z-probes. Neighbor-read reverse fails because
holonomy fails from split fail at `A` and at `D` of the `x=1` yz square.
Neighbor-read face fails because holonomy fails from split fail at `C2`
and at `C3` of the `x=2` yz square from mixed two-axis `M` and empty `O`.
nm2holyz2x reverse fails from the product at `S` alone from singleton
`M={−e_3}`; this reverse is neighbor-read of that square on the far-face
seed. nm2holyz2n reverse fails even though the `−e_1` translate HOLDs on
the two-axis seed; here that translate fails. nm2holyz2xf reverse fails
from the product at `S` alone on this seed. nm2holyz reverse HOLDs on the
two-axis seed because the product of the four edge sendings around the
`x=0` yz square is the identity; on this far-face seed that square fails,
and that square is not scored here. Transport reverse HOLDs and transport face
HOLDs on the z-probes: leftover of nm2cycfrmz cyclic-frame transport, not
this neighbor-read. nm2cycfrmhol xy-square holonomy reverse HOLDs and face
fails on different vertices. Scalar neighbor-read of Orient fails at
reverse `A` and at reverse `D`; that is not the four-edge product.
HOLDING cyclic #7451/#7452 Orient reverse HOLDs from equal signs without
a four-edge product; this reverse fails. Unique nonnegative permutation
sending fails at each reverse vertex. Cover and split fail at reverse
`A,D` as this reverse fails, from a different object; cover and split
HOLD at face `C,C1` while this face fails at `C2,C3`. Leftover of the
union at reverse `A,D` is `{e_2}`, so leftover reverse HOLDs while this
reverse fails. Leftover-axis reverse HOLDs with `−1,−1` on the z-probes
and face fails with `+1,−1` because C and D swap `(m,pair)` columns;
those two signs are not `P12 P23 P34 P41`. Lex-one reverse fails from
`e1<e2<e3` order independent of `m`; this reverse fails from split fail
at `A,D`. Lexicographic unsigned `o1,o2` reverse fails with `−1,+1` and
face HOLDs with `+1,+1` on the z-probes. Unique signed `|O_i|=1` reverse
fails on the z-probes as this reverse fails, from a different object.
Cyclic lex-smallest reverse HOLDs with `+1,+1` and face HOLDs with
`−1,−1` on the z-probes; those signs are not these holonomy bits.
Presence of an opposite pair in `O` HOLDs at each of the four z-probes
without cyclic columns. Unique outgoing letters would assign `UNDEFINED`
at mixed `O(B)`; this Orient at reverse `B` is `−1`, not `UNDEFINED`. On
unique signed `O={+e_1,+e_3}` leftover is empty while Orient is `+1`, so
leftover-empty fail is not this predicate. Mixed #7188 is a different
z-symmetric process with mixed `M`. The second pair is a new seed, not a
formed child: `(0,0,1)` is recorded at tick 0 with lock `+e_2`, whereas
the 1-axis child forms at tick 1 with lock `+e_3`. The third pair is a
new seed, not a formed child: `(0,0,−1)` is recorded at tick 0 with lock
`+e_3`. Reverse neighbor-read is HOLD iff holonomy of the `x=1` square
HOLDs and some formed 6-NN translate also HOLDs, not leftover of
leftover-axis and not leftover of nm2holyz x=0 reverse HOLD.

### N8 — cross-cycle echo

nm2axz cover on this three-axis far-face seed reported cover HOLD at each of the four
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
The four y-probes of this same seed reported cyclic Orient `+1` at `A`
from `m=−e_1` and Orient fail at `D` from split fail, so y-reverse fails
and y-face fails. nm2oricyclz cyclic next/prev lex-largest Orient on the
same seed reported HOLDING cyclic #7451/#7452 with Orient `−1,−1,+1,+1`,
reverse hold, and face hold from equal signs, without a sending matrix.
This note is not those displays: it reports neighbor-read of cyclic-frame holonomy of
`(m,o_next,o_prev)` of `M` and `O` at `τ=t+1` around the x=1 yz unit
square on the three-axis far-face opposite seed, with `t(A)=2`, `t(D)=2`, `t(B)=1`,
`t(E)=1`, `t(C)=3`, `t(C1)=3`, `t(C2)=4`, and `t(C3)=4`, reverse neighbor-read
fail, and face neighbor-read fail, while nm2holyz reverse HOLDs on the x=0
square on the two-axis seed and fails on this far-face seed, while nm2holyz2n
reverse fails with a HOLDING `−e_1` translate, while nm2cycfrmhol xy-square holonomy reverse HOLDs and face fails
on different vertices, while nm2cycfrmz transport reverse HOLDs and
transport face HOLDs on the z-probes. Cover and split do not score
handedness.

**Gate disposition:** PASS for the cyclic-frame-holonomy `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
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
scalar neighbor-read of Orient HOLD,” “the predicate equals unique
nonnegative permutation sending HOLD,” “the predicate equals nmcover
axis-cover HOLD,” “the predicate equals nm2axz axis-cover HOLD,” “the
predicate equals nm2ax12z 1-in 2-out split HOLD,” “the predicate equals
the 1-axis opposite two-site seed,” “the predicate equals nmunopp union,”
“bits are Admissibility,” “split fail is UNDEFINED,” or “empty `O_i` is
UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis far-face opposite
perp-step incoming-lock process, reads each square vertex's own earliest
incoming set and own outgoing dual from the record prefix at that vertex's
`t+1`, reports split of the pair, reports the cyclic frame
`F=(m,o_next,o_prev)` as nm2cycfrmhol, reports Orient as nm2oricyclz
lex-largest cyclic, reports `P` on each formed six-neighbor edge of the
reverse yz square `A-D-B-E` at `x=1` and of the face yz square
`C-C1-C2-C3` at `x=2`, reports the holonomy products, reports neighbor-read
of those squares, lists new records
in `B_3(0)` between `t` and `t+1` that meet a vertex's six-neighbors, and
checks Theorems 1--3. It also
checks that reverse neighbor-read fails and face neighbor-read fails, that the x=0
square is not scored, that a vertex outside `B_3(0)` is fail not
`UNDEFINED`, that nm2holyz reverse HOLDs on x=0 on the two-axis seed while
this reverse fails and that x=0 square fails on this far-face seed,
that nm2holyz2n reverse fails while its `−e_1` translate HOLDs,
that nm2cycfrmz transport reverse HOLDs and transport face HOLDs while
holonomy reverse fails and holonomy face fails, that leftover reverse
HOLDs at `A,D` while holonomy reverse fails, that split fail is holonomy
fail not `UNDEFINED`, that empty `O_next` or empty `O_prev` is Orient fail
not `UNDEFINED`, that mixed two-axis `M` at `C2,C3` is holonomy fail not
`UNDEFINED`, that mixed `M={±e_3}` at `A,D` is holonomy fail not
`UNDEFINED`, that the 1-axis opposite two-site seed is a different member
with `t(A)=3`, that #7477 same-lock is a different member, that LIVE
three-axis as a three-site seed is a different member, that leftover-empty
fail is a different predicate, that leftover of `M` alone and leftover of
`O` alone are different objects, that mixed sets remain sets, that the
construction does not sum, that a formation member from already-recorded
six-neighbor locks is not attached, that the second pair is a new seed not
a formed child, that the third pair is a new seed not a formed child, that
the y-probes and x-probes of this seed are not this letter, and that the
display is not the two-tick lock-count clock
composition. No runner cache is written.
