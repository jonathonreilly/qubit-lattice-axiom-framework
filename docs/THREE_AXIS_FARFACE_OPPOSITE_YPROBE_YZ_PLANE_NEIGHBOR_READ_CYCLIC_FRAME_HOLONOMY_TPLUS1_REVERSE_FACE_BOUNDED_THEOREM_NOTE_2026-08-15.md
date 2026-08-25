---
claim_id: three_axis_farface_opposite_yprobe_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of yz-plane cyclic-frame holonomy at t+1 on the four y-probes of the three-axis far-face opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_farface_opposite_yprobe_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Yz-Plane Cyclic-Frame Holonomy At t+1 Reverse And Face On Four Y-Probes Of The Three-Axis Far-Face Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of cyclic-frame holonomy around the yz-plane unit
square of simultaneous earliest incoming set `M` and outgoing dual `O` at
each vertex's `τ=t+1`, scored at the four y-probe translates of that square,
and reverse/face from that neighbor-read, on the three-axis
far-face opposite seed in `B_3(0)={n:n·n<=9}`. y-probes as nm2ax. y-probes as
nm2sfzrdy: `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`. `F` and
Orient as nm2cycfrmhol. Yz squares and neighbor-read as nm2holyzrd. For
each probe `q`, `S(q)` is the yz unit square with a vertex at `q` if that
square lies in `B_3(0)`; else fail, not `UNDEFINED`. Neighbor-read of
holonomy of `S(q)` as nm2holyzrd. Reverse `A,B`. Face `C,D`. Drop any
vertex outside `B_3(0)` as fail, not `UNDEFINED`. Let `t(q)` be the
formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of
earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing
dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed
and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Axis of a defined lock set `S` is
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
neighbor-read of `S(A)` and of `S(B)` HOLDs. Face HOLDs if and only if
neighbor-read of `S(C)` and of `S(D)` HOLDs. Face is displayed, not
adopted. Cover and split do not score handedness. This is not leftover of
nm2yzrdfz neighbor-read of yz holonomy reverse fail face fail on the
untranslated yz squares `A-D-B-E` at `x=0` and `C-C1-C2-C3` at `x=1`: that
letter scores those two squares of this same far-face seed, while this
letter scores the four y-probe translates; parent reverse fails here as
leftover, coincidentally matching this reverse fail on different squares.
This is not leftover of nm2yzrd3y near-face y-probe yz neighbor-read fail/fail:
those y-probes are the same four sites on the near-face third pair
`(2,0,0)/(2,1,0)`, whose untranslated reverse HOLDs, while this far-face
third pair is `(0,0,−1)/(0,1,−1)` and untranslated reverse fails. This is
not leftover of nm2yzrdy two-axis y-probe yz neighbor-read fail/fail #7588:
those y-probes sit on four tick-0 two-axis seeds whose unit-square reverse
HOLDs #7563, while this reverse fails on six tick-0 far-face seeds. This is
not leftover of nm2yzrd3x x-probe yz neighbor-read: those
probes are `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`, and `S` of
x-probe `A` is the face square of nm2yzrdfz, while `S` of y-probe `A` is
the `+e_2` translate of the reverse square; x-probe `C` lies in `B_3(0)`
while y-probe `S(C)` does not. This is not leftover of nm2holyzrd two-axis
yz neighbor-read reverse HOLD face fail: those neighbor-read bits are
HOLD/fail on four tick-0 seeds, not fail/fail on the four y-probe
translates of this far-face seed. This is not leftover of nm2cycfrmhol xy-square holonomy reverse HOLD face
fail: those vertices are the `z=1` square, not these y-probe yz squares.
This is not leftover of nm2holyz
yz-square holonomy: nm2holyz scores the product at `S` alone. This is not
leftover of nm2sfzrdy neighbor-read of cyclic-frame transport reverse
HOLD face fail on these same y-probes: transport neighbor-read HOLDs at
`A,B,C` and fails at `D`, so that reverse HOLDs while this reverse fails
because own-square holonomy fails at both `S(A)` and `S(B)`. This is not
leftover of nm2cycfrmz cyclic-frame transport reverse HOLD face HOLD:
transport is existential at a vertex, holonomy is the product around a
square. This is not leftover of scalar neighbor-read of Orient. This is
not leftover of a unique nonnegative permutation sending. This is not
leftover of nm2orichy leftover-axis reverse fail. This is not leftover of
nm2orioney lex-one reverse fail from `e1<e2<e3` order independent of `m`.
This is not leftover of nm2chiraly lexicographic unsigned `o1,o2`
orientation. This is not leftover of unique signed outgoing letters. This
is not leftover of nm2ax axis-cover. This is not leftover of nm2ax12 1-in
2-out split. This is not leftover of leftover-of-`M` alone. This is not leftover of
leftover-of-`O` alone. This is not leftover-empty fail of leftover axis.
This is not leftover of nmunopp union. This is not leftover of nmt2opp `M`
frozen at `t`. This is not leftover of nmot2opp two-tick composition. This
is not leftover of nmoutopp untimed eventual-`O`. This is not leftover of
mixed #7188 fail/fail. This is not leftover of the 1-axis opposite two-site
seed. This is not leftover of the same-lock two-site seed. The second pair is
a new seed, not a formed child. The third pair is a new seed, not a formed
child. Uniqueness is not required. Mixed remains a set. Displayed, not adopted.
Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_farface_opposite_yprobe_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_farface_opposite_yprobe_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probe yz-plane unit squares. Neighbor-read of holonomy is as
nm2holyzrd, on those yz squares translated so a vertex sits at each y-probe of
nm2sfzrdy. Incoming lock letters are unit nearest-neighbor
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
on neighbor-read HOLD of `S(A)` and `S(B)`, and of `S(C)` and `S(D)`.
Holonomy of nm2holyz is a different readout: it scores the product at `S`
alone. Neighbor-read of the untranslated yz squares is leftover of
nm2yzrd3z. Neighbor-read of the four x-probe translates is leftover of
nm2yzrd3x. Transport of nm2cycfrmz
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
claim_type_reason: "Exact report of neighbor-read of cyclic-frame holonomy around the yz-plane unit square of M and O at t+1 on the four y-probes of the three-axis far-face opposite seed, S(q) at A,B,C,D, holonomy and neighbor-read of those squares, reverse fail and face fail from neighbor-read of S(A),S(B) and of S(C),S(D); uniqueness of a sending is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_farface_opposite_yprobe_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face
target_blocker_text: "display neighbor-read of yz-plane cyclic-frame holonomy reverse/face on the four y-probes of the three-axis far-face opposite seed, not leftover of nm2yzrd3z untranslated yz squares, not leftover of nm2yzrd3x x-probe yz neighbor-read, not leftover of nm2holyzrd two-axis yz neighbor-read, not leftover of nm2holyz yz-square holonomy, not leftover of nm2sfzrdy neighbor-read of cyclic-frame transport, not leftover of nm2cycfrmz transport, not scalar neighbor-read of Orient, not unique nonnegative sending, not leftover-axis, not lex-one e1<e2<e3, not unique |O_i|=1, not unsigned axis units, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of cyclic-frame holonomy of F around the y-probe yz-plane unit squares at t+1 displayed; do not write holonomy into Admissibility, do not reduce to nm2yzrd3z untranslated yz squares, do not reduce to nm2yzrd3x x-probe yz neighbor-read, do not reduce to nm2holyzrd two-axis yz neighbor-read, do not reduce to nm2holyz yz-square holonomy, do not reduce to nm2sfzrdy neighbor-read of cyclic-frame transport, do not reduce to nm2cycfrmz transport, do not reduce to scalar neighbor-read of Orient, do not reduce to unique nonnegative permutation sending, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-smallest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace holonomy by unique outgoing letters, do not replace holonomy by existential opposite of signed locks, do not replace holonomy by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of cyclic-frame holonomy around the yz-plane unit square of M and O at t+1 on the four y-probes of the three-axis far-face opposite seed and reverse/face from that neighbor-read; displayed, not adopted"
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

No larger host is used. The four y-probe translates of the nm2holyzrd yz
unit square are the only cycles whose neighbor-read of cyclic-frame
holonomy of `F=(m,o_next,o_prev)` of `M` and `O` is scored as this letter:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
S(q) = q, q+e_2, q+e_2+e_3, q+e_3.
S(A) = (0, 1, 0), (0, 2, 0), (0, 2, 1), (0, 1, 1)
S(B) = (1, 1, 1), (1, 2, 1), (1, 2, 2), (1, 1, 2)
S(C) = (0, 2, 0), (0, 3, 0), (0, 3, 1), (0, 2, 1)
S(D) = (1, 1, 0), (1, 2, 0), (1, 2, 1), (1, 1, 1)
```

A vertex outside `B_3(0)` is fail, not `UNDEFINED`. `S(C)` lies outside
`B_3(0)` because `(0,3,1)·(0,3,1)=10>9`. These y-probes are not the
x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`. These are not
the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`, `D=(1,0,1)`. Same
process as nm2ax. `F` and Orient as nm2cycfrmhol. Neighbor-read of holonomy
as nm2holyzrd on each `S(q)`. Reverse `A,B`. Face `C,D`. The untranslated
yz squares of nm2yzrd3z remain leftover:

```text
A = (0,0,0),  D = (0,1,0),  B = (0,1,1),  E = (0,0,1).
C = (1,0,0),  C1 = (1,1,0),  C2 = (1,1,1),  C3 = (1,0,1).
```

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. Site `(0,0,−1)` locks `+e_3`. Site `(0,1,−1)`
locks `−e_3`. The second pair is a new seed, not a formed child of the
first pair. The third pair is a new seed, not a formed child: it is the
far-face seed of nm2yzrdfz. This seed is
not the two-axis opposite seed of nm2holyzrd. This seed is not the 1-axis
opposite two-site seed `{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is
not the perp two-site seed `+e_1/+e_2`. This seed is not the same-lock
two-site seed `+e_1/+e_1`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site seed
that also records `(0,-1,0)` at tick 0. This seed is not the LIVE
three-axis three-site seed.

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
If S does not lie in B_3(0), neighbor-read fails, not UNDEFINED.
Uniqueness of a sending neighbor is not required.
Uniqueness of a holonomy-HOLDING translate is not required.
```

Neighbor-read of the scalar Orient sign HOLDs at `q` if and only if
`Orient(q)` is `±1` and some formed six-neighbor has the same sign. That
is a different object. Transport of nm2cycfrmz HOLDs at `q` if and only if
some formed six-neighbor hosts a signed-permutation sending. That is a
different object: transport HOLDs at `A,B,C` and fails at `D` on these
y-probes, so transport reverse HOLDs while this reverse fails. Neighbor-read
of that transport is leftover of nm2sfzrdy. Holonomy of nm2yzrd3z
untranslated reverse square HOLDs and face fails. A mutation that scored
only a holonomy-HOLDING 6-NN translate of `S(A)`, ignoring holonomy at
`S(A)`, would HOLD at `A` because the `−e_2` translate is the reverse
square of nm2yzrd3z whose holonomy HOLDs. Neighbor-read of xy holonomy on
the three-axis far-face seed fails reverse and face. A unique nonnegative
permutation sending is a different object and fails at `A` and at `B`.

Reverse neighbor-read cyclic-frame holonomy holds if and only if
neighbor-read of `S(A)` and of `S(B)` HOLDs. Face neighbor-read
cyclic-frame holonomy holds if and only if neighbor-read of `S(C)` and of
`S(D)` HOLDs. If holonomy of a square fails, neighbor-read of that square
fails, not `UNDEFINED`. If `S(C)` lies outside `B_3(0)`, face fails, not
`UNDEFINED`.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse without reading the four-edge
product. Identifying split reverse with this reverse is refused: split
HOLDs reverse without the four-edge product. Identifying leftover-empty
fail with this reverse is refused: leftover-empty fail scores empty leftover
as reverse fail coincidentally, but leftover-empty is unsigned unoccupied
directions, not own-square holonomy plus a translate. Identifying nm2holyz
yz-square holonomy with this reverse is refused: nm2holyz scores the
product at `S` alone. Identifying nm2yzrd3z with this reverse is refused:
that reverse HOLDs on the untranslated `x=0` square. Identifying
nm2sfzrdy with this reverse is refused: that reverse HOLDs from
existential transport neighbor-read. Identifying lexicographic unsigned
`o1,o2` with this reverse is refused: unsigned reverse fails from
`Orient(A)=−1` while this reverse fails from own-square holonomy fail.
Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis.

## Theorem 1 — ticks, squares, holonomy, neighbor-read at `A,B,C,D`

On this process the four y-probes form in `B_3(0)`. Compare to leftover
axis: that leftover reports empty leftover at each probe and leftover
reverse fail and leftover face fail. Compare to nm2ax cover and nm2ax12
split: cover and split HOLD reverse and fail face on this member, matching
face bits without scoring handedness; cover reverse HOLDs while this
reverse fails. Compare to nm2oricyclz cyclic Orient: reverse HOLDs from
equal `+1` signs without a four-edge product. Compare to nm2cycfrmz
cyclic-frame transport: reverse HOLDs and face fails from existential
sendings. Compare to nm2sfzrdy neighbor-read of that transport: reverse
HOLDs and face fails. Compare to scalar neighbor-read of Orient: HOLD at
`A`, `B`, and `C`, fail at `D`, so scalar reverse HOLDs while this reverse
fails. Compare to nm2chiraly lexicographic unsigned `o1,o2` orientation:
reverse fails from unsigned `Orient(A)=−1`. Compare to unique signed
outgoing letters: unique signed HOLDs at `A` and at `B` and fails at `C`
and at `D`. Compare to nm2orichy leftover-axis, which fails at `A` and at
`B` because those outgoing sets have no opposite pair. Compare to
nm2orioney lex-one reverse fail from `e1<e2<e3` order independent of `m`.
This display reads neighbor-read of the cyclic-frame holonomy of
`(m,o_next,o_prev)` around the four y-probe yz-plane unit squares of those
same timed sets:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
S(A) = (0, 1, 0), (0, 2, 0), (0, 2, 1), (0, 1, 1)
S(B) = (1, 1, 1), (1, 2, 1), (1, 2, 2), (1, 1, 2)
S(C) = (0, 2, 0), (0, 3, 0), (0, 3, 1), (0, 2, 1)
S(D) = (1, 1, 0), (1, 2, 0), (1, 2, 1), (1, 1, 1)
S(C) lies outside B_3(0)
holonomy(S(A)) = fail
holonomy(S(B)) = fail
holonomy(S(C)) = fail
holonomy(S(D)) = fail
neighbor-read(S(A)) = fail
neighbor-read(S(B)) = fail
neighbor-read(S(C)) = fail
neighbor-read(S(D)) = fail
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
det(B) = −1
Orient(B) = −1
m(C) = +e_2
i(C) = 2
o_next(C) = +e_3
o_prev(C) = −e_1
det(C) = 1
Orient(C) = −1
Orient(D) = fail
F(A) = (−e_1, +e_2, −e_3)
F(B) = (+e_1, +e_2, −e_3)
F(C) = (+e_2, +e_3, −e_1)
F(D) = fail
P on S(A) = [0 0 1; 1 0 0; 0 -1 0], fail, fail, [0 -1 0; 0 0 -1; 1 0 0]
```

Leftover untranslated yz squares of nm2yzrd3z, not this letter:

```text
neighbor-read(A-D-B-E) = fail
neighbor-read(C-C1-C2-C3) = fail
holonomy(A-D-B-E) = fail
holonomy(C-C1-C2-C3) = fail
```

`A` is a seed at tick 0 with seed letter `−e_1`. Mixed remains a set:
`O(C,τ)` has three outgoing steps. Unique outgoing letters would assign
`UNDEFINED` at mixed `O`. Unique signed `|O_i|=1` fails at `C` because
the `e_1` cyclic slot has both signs. Lex-largest picks `−e` on that mixed
cyclic slot, so `(o_next,o_prev)` is defined at `C`. `M` is a singleton
at each of `A,B,C` and mixed `{+e_3,−e_3}` at `D`. Split HOLDs at `A,B,C`
and fails at `D` from `|Axis(M)|=2`. Cover and split HOLD reverse and do
not score that own-square holonomy fails. At `A`, `i=1` so `e_next=e_2` and
`e_prev=e_3`; `O` is `{+e_2,−e_3}` with no opposite pair. At `B`, mixed
`O` has both signs of `e_3`, so unique signed fails while lex-largest
picks `−e_3` and Orient is `−1`. At `D`, mixed `M={+e_3,−e_3}` and
`O={+e_1,−e_1}` so cover fails, split fails, and Orient fails, not
`UNDEFINED`. O is not M.

On the 1-axis opposite two-site seed, `t(D)=3` while here `t(D)=2`. That
is leftover of the first pair. The third pair is a new seed, not a formed
child. On the y-probes of this same seed, transport reverse HOLDs from
existential sendings, leftover of nm2sfzrdy, not this yz square. On the
x-probes, `S` of x-probe `A` is the face square of nm2yzrdfz, leftover of
nm2yzrd3x, not this letter.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,0)` is a
seed, so it is not a new 6-NN of `A`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is `{−e_3}` at `A` and empty
at `B,C`, split fails, Orient is fail, not UNDEFINED, and the cyclic frame
fails, not UNDEFINED. At `D`, `O` at `t` is `{−e_1}` and Orient is fail,
not UNDEFINED. Transport at `t` therefore fails, not UNDEFINED.

Each of `A,B,C` has a formed six-neighbor with split HOLD and a signed
permutation sending. Uniqueness of that neighbor is not required. First
witness in six-neighbor order: `A` sends to `C=(0,2,0)` with `det(P)=1`.
Scalar neighbor-read HOLDs at `A,B,C`. Those existential transport bits
are leftover of nm2cycfrmz cyclic-frame transport, not this neighbor-read.
Own-square holonomy of `S(A)` fails because `(0,2,1)` is split fail, so
neighbor-read of `S(A)` fails, not `UNDEFINED`, even though the `−e_3`
translate of `S(A)` has holonomy HOLD (a mutation ignoring holonomy at
`S(A)` would HOLD at `A`). The `−e_2` translate of `S(A)` is the reverse
square of nm2yzrdfz and has holonomy fail. Own-square holonomy of `S(B)`
fails from split fail at three of four vertices. `S(C)` does not lie in
`B_3(0)`, so holonomy and neighbor-read fail, not `UNDEFINED`. Own-square
holonomy of `S(D)` fails from split fail at three of four vertices,
including probe `D`. This is not leftover of nm2yzrdfz: that reverse also
fails, but on the untranslated `x=0` square. This is not leftover of
nm2holyz: that scores holonomy at `S` alone. This is not leftover of
nm2sfzrdy: that reverse HOLDs.

## Theorem 2 — reverse from neighbor-read of cyclic-frame holonomy at `τ`

Reverse neighbor-read cyclic-frame holonomy holds if and only if
neighbor-read of `S(A)` and of `S(B)` HOLDs. Own-square holonomy fails at
both `S(A)` and `S(B)`, so neighbor-read fails at both, not `UNDEFINED`.
Reverse fails. This is HOLD iff neighbor-read of both reverse probes
HOLDs, not leftover of nm2yzrdfz untranslated far-face yz neighbor-read,
not leftover of nm2yzrd3y near-face y-probe yz neighbor-read, not leftover
of nm2yzrdy two-axis y-probe yz neighbor-read, not leftover of nm2yzrd3z
untranslated yz neighbor-read, not leftover of nm2yzrd3x x-probe yz
neighbor-read, not leftover of nm2holyzrd two-axis yz neighbor-read, not
leftover of nm2holyz yz-square holonomy, not leftover of nm2sfzrdy
neighbor-read of cyclic-frame transport, not leftover of
nm2cycfrmz cyclic-frame transport, not leftover of nm2oricyclz cyclic
Orient equal signs, not leftover of scalar neighbor-read, not leftover of
a unique nonnegative permutation sending, not leftover of nm2chiraly
lexicographic unsigned `o1,o2`, not leftover of nm2oridetz unique signed
outgoing letters, not leftover of nm2orichy leftover-axis, not leftover of
nm2orioney lex-one, not leftover of nm2ax axis-cover, not leftover of
nm2ax12 1-in 2-out split, not leftover-empty fail, and not exist-opposite.

Reverse neighbor-read cyclic-frame holonomy at τ: fail

Both squares at `A` and at `B` are in `B_3(0)`, so this is not `UNDEFINED`.
Cover reverse HOLDs because cover HOLDs at `A` and at `B`. Split reverse
HOLDs because split HOLDs at `A` and at `B`. Cover and split do not score
handedness. nm2cycfrmz transport reverse HOLDs because transport HOLDs at
`A` and at `B`; that is existential at two vertices, not the four-edge
product. nm2sfzrdy neighbor-read of that transport reverse HOLDs. Scalar
reverse fails because scalar fails at `B`. Orient reverse fails from
`+1` at `A` and `−1` at `B`. Unique nonnegative reverse fails. Leftover-axis
reverse fails because leftover-axis at `A` fails (no opposite pair in `O`).
Lexicographic unsigned reverse HOLDs coincidentally from unsigned
`Orient(A)=−1` and `Orient(B)=−1`, while this reverse fails. Unique signed
reverse fails because unique signed fails at mixed `O(B)`. Lex-one signed
reverse fails because lex-one `Orient(A)=−1` and `Orient(B)=+1`. Cyclic
lex-smallest reverse HOLDs with
equal signs `+1,+1`. Leftover-empty reverse fails because leftover of the
union is empty at `A` and at `B`. Leftover of `M` reverse HOLDs because
leftover of `M` at `A` and at `B` is `{e_2,e_3}`: nonempty and equal, while
this reverse fails. Leftover of `O` reverse HOLDs because leftover of `O`
at `A` and at `B` is `{e_1}`. Exist-opposite reverse of signed `M` HOLDs
because `M(A)={−e_1}` and `M(B)={+e_1}`. Exist-opposite reverse of signed
`O` HOLDs. Presence of an opposite pair in `O` fails at `A` and HOLDs at
`B`. Those leftovers are not this display. nm2yzrdfz reverse fails on the
untranslated square, leftover of a different pair of squares. nm2holyzrd
two-axis unit-square reverse HOLDs #7563. A mutation ignoring holonomy at
`S(A)` would HOLD at `A` from the `−e_3` translate.

Reverse fails.

## Theorem 3 — face from neighbor-read of cyclic-frame holonomy at `τ`

Face neighbor-read cyclic-frame holonomy holds if and only if neighbor-read
of `S(C)` and of `S(D)` HOLDs. `S(C)` lies outside `B_3(0)` because
`(0,3,1)·(0,3,1)=10>9`, so holonomy of `S(C)` fails, not `UNDEFINED`, and
neighbor-read of `S(C)` fails, not `UNDEFINED`. Split fails at `D`, so
holonomy of `S(D)` fails and neighbor-read of `S(D)` fails, not
`UNDEFINED`. Face fails. Displayed, not adopted.

Face neighbor-read cyclic-frame holonomy at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Transport face fails because transport fails at `D`.
Orient face fails because Orient fails at `D`. Scalar face fails. Unique
signed face fails. nm2yzrd3z face fails on the untranslated `x=1` square
from split fail at `C1`. nm2yzrd3x face fails on the x-probe translates,
but x-probe `S(C)` lies in `B_3(0)` while this `S(C)` does not. A vertex
outside `B_3(0)`, for example the parallel yz square at `x=4`, is holonomy
fail, not `UNDEFINED`.

Face fails.

## What this note does not claim

- It does not replace neighbor-read by nm2yzrd3z neighbor-read of yz holonomy.
- It does not replace neighbor-read by nm2yzrd3x x-probe yz neighbor-read.
- It does not replace neighbor-read by nm2holyzrd two-axis yz neighbor-read.
- It does not replace neighbor-read by nm2holyz yz-square holonomy.
- It does not replace neighbor-read by nm2sfzrdy neighbor-read of cyclic-frame transport.
- It does not replace holonomy by nm2cycfrmz cyclic-frame transport.
- It does not replace holonomy by neighbor-read of the scalar Orient sign.
- It does not replace holonomy by a unique nonnegative permutation sending.
- It does not require a unique formed six-neighbor witness.
- It does not reprint nm2oricyclz cyclic Orient reverse hold as this holonomy.
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
- It does not reprint nmcover axis-cover reverse hold as this
  oriented display.
- It does not reprint nm2ax axis-cover reverse hold as this
  oriented display.
- It does not reprint nm2ax12 1-in 2-out split reverse hold as
  this oriented display.
- It does not reprint nm2chiraly lexicographic unsigned `o1,o2` reverse fail
  as this oriented display.
- It does not reprint nm2oridetz unique signed reverse hold as
  this oriented display.
- It does not reprint nm2orichy leftover-axis reverse fail as
  this oriented display.
- It does not reprint nm2orioney lex-one reverse fail as this oriented display.
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

This display uses Lattice to name `B_3(0)` and the four y-probe unit squares.
It uses Qubit only as the algebra of the local possibility domain. It uses
Record only as a boundary: a present lock is content. It does not rewrite
Admissibility. The three-axis far-face opposite seed process, neighbor-read
of cyclic-frame holonomy of `(m,o_next,o_prev)` of `M` and `O` at `t+1`
around the y-probe yz-plane unit squares, and the reverse/face bits from
that neighbor-read are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three-axis far-face opposite seed `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `S(A)`, `S(B)`, `S(C)`, `S(D)` | Theorem 1; yz unit squares; `S(C)` outside `B_3(0)` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; HOLD at `A,B,C`; fail at `D` |
| unique signed `m`, axis index `i`, cyclic `(o_next,o_prev)` | Theorem 1; singleton `M`; lex-largest pair defined at `A,B,C` |
| integer `det(m,o_next,o_prev)` | Theorem 1; `1`, `1`, `1` at `A,B,C` |
| Orient at `τ` | Theorem 1; `+1,+1,+1`, fail |
| cyclic frame `F=(m,o_next,o_prev)` | Theorem 1; LIVE three-axis at `A,B,C`; fail at `D` |
| holonomy of `S(A)`, `S(B)`, `S(C)`, `S(D)` | Theorem 1; fail, fail, fail, fail |
| neighbor-read of `S(A)`, `S(B)`, `S(C)`, `S(D)` | Theorem 1; fail, fail, fail, fail |
| leftover of nm2yzrd3z untranslated yz neighbor-read | Theorem 1; reverse hold and face fail on `A-D-B-E` and `C-C1-C2-C3` |
| leftover of nm2yzrd3x x-probe yz neighbor-read | Theorem 1; fail/fail on different squares; x-probe `C` in host |
| leftover of nm2holyzrd two-axis yz neighbor-read | Theorem 1; reverse hold and face fail with four tick-0 seeds |
| leftover of nm2holyz yz-square holonomy | Theorem 1; product at `S` alone |
| leftover of nm2sfzrdy neighbor-read of cyclic-frame transport | Theorem 1; reverse hold and face fail on these y-probes |
| leftover of nm2cycfrmz cyclic-frame transport | Theorem 1; transport reverse hold and transport face fail |
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
| leftover of nm2ax axis-cover HOLD | not this oriented display |
| leftover of nm2ax12 1-in 2-out split HOLD | not this oriented display |
| leftover of nm2chiraly lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichy leftover-axis | not this oriented display |
| leftover of nm2orioney lex-one signed `e1<e2<e3` | not this oriented display |
| leftover of cyclic lex-smallest | not this oriented display |
| leftover of nm2oricyclz cyclic Orient equal signs | not this holonomy |
| leftover of nm2cycfrmz cyclic-frame transport | not this holonomy |
| leftover of nm2holyzrd two-axis yz neighbor-read | not these y-probe squares |
| leftover of nm2yzrd3z neighbor-read of yz holonomy | not these y-probe squares |
| leftover of nm2yzrd3x x-probe yz neighbor-read | not these y-probe squares |
| leftover of nm2holyz yz-square holonomy | not this neighbor-read |
| leftover of nm2sfzrdy neighbor-read of cyclic-frame transport | not this holonomy |
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
| leftover of the LIVE three-axis three-site seed | not this display |
| split fail scored as `UNDEFINED` | refused; Orient fail |
| empty `O_i` scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of cyclic-frame holonomy around the yz-plane unit square of `(m,o_next,o_prev)` of `M` and `O` at `t+1` on the four y-probes of the three-axis far-face opposite seed, and reverse/face from that neighbor-read. |
| V2 | Current main has no landed neighbor-read of yz-plane cyclic-frame-holonomy reverse/face of timed `M` and `O` on these four y-probe yz-plane unit squares of the three-axis far-face opposite seed. |
| V3 | Four y-probe squares, holonomy of those squares, neighbor-read of those squares, and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads neighbor-read of the four-edge signed-permutation product around the y-probe yz-plane unit squares at the same `t+1` cut, reverse fails and face fails while nm2yzrd3z neighbor-read reverse HOLDs and face fails on the untranslated squares, nm2yzrd3x x-probe reverse fails and face fails on different squares with `S(C)` in host, nm2holyzrd two-axis yz neighbor-read reverse HOLDs and face fails, nm2sfzrdy transport neighbor-read reverse HOLDs and face fails, nm2cycfrmz transport reverse HOLDs, scalar neighbor-read reverse HOLDs, unique nonnegative sending fails at `A` and at `B`, and nm2oricyclz Orient equality HOLDs reverse without the product. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by nm2chiraly lexicographic unsigned `o1,o2`, does not replace
Orient by nm2oridetz unique signed `|O_i|=1`, does not replace Orient by
nm2orichy leftover-axis, does not replace Orient by nm2orioney lex-one,
does not replace Orient by cyclic lex-smallest, does not replace Orient by
nmcover axis-cover, does not replace Orient by nm2ax axis-cover, does not
replace Orient by nm2ax12 1-in 2-out split, does not identify this
display with the 1-axis opposite two-site seed, and does not identify it
with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| scalar neighbor-read of Orient | reuse equal Orient sign at some formed 6-NN | scalar HOLDs at `A`, `B`, and `C` and fails at `D`; scalar reverse HOLDs while this reverse fails | ATTEMPTED |
| unique nonnegative permutation sending | require a unique sending with no minus signs | unique nonnegative sending fails at `A` and at `B`; uniqueness is not required | ATTEMPTED |
| nm2yzrd3z untranslated yz neighbor-read | reuse neighbor-read reverse hold and face fail of `A-D-B-E` and `C-C1-C2-C3` | nm2yzrd3z reverse HOLDs on the `x=0` square of four seeds; this reverse fails on `S(A)` and `S(B)` | ATTEMPTED |
| nm2yzrd3x x-probe yz neighbor-read | reuse fail/fail on the four x-probe translates | x-probe `S(A)` is the face square; x-probe `S(C)` lies in `B_3(0)`; this `S(A)` is the `+e_2` translate of the reverse square and this `S(C)` lies outside | ATTEMPTED |
| nm2holyzrd two-axis yz neighbor-read | reuse neighbor-read reverse hold and face fail of the same two yz squares | nm2holyzrd reverse HOLDs and face fails from empty cyclic slots at `C` and `C1` with `t(C)=2`; this reverse fails on six tick-0 seeds | ATTEMPTED |
| nm2holyz yz-square holonomy | reuse holonomy reverse hold and face fail of the same two yz squares | nm2holyz reverse HOLDs and face fails from the product at `S` alone; this reverse requires a formed 6-NN translate whose holonomy HOLDs after own HOLD | ATTEMPTED |
| nm2sfzrdy neighbor-read of cyclic-frame transport | reuse neighbor-read reverse hold and face fail on these y-probes | that reverse HOLDs from existential transport at `A` and at `B`; this reverse fails from own-square holonomy fail | ATTEMPTED |
| nm2cycfrmz cyclic-frame transport | reuse transport reverse hold from existential 6-NN sendings | transport reverse HOLDs while this reverse fails; transport is existential at a vertex, holonomy is the four-edge product | ATTEMPTED |
| nm2oricyclz cyclic Orient | reuse Orient reverse hold from equal `±1` signs | Orient reverse HOLDs (`A` `+1`, `B` `+1`) without a four-edge product; this reverse fails | ATTEMPTED |
| nm2chiraly lexicographic unsigned `o1,o2` | reuse unsigned reverse fail | unsigned reverse fails while this reverse fails from a different object: own-square holonomy, not unsigned columns | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse hold | unique signed reverse HOLDs coincidentally at `A` and at `B` while this reverse fails | ATTEMPTED |
| nm2orichy leftover-axis | reuse leftover-axis reverse fail | leftover-axis reverse fails because leftover-axis at `A` and at `B` fails; those two signs are not `P12 P23 P34 P41` | ATTEMPTED |
| nm2orioney lex-one | reuse lex-one reverse fail | lex-one reverse fails from `e1<e2<e3` order independent of `m`; this reverse fails from own-square holonomy | ATTEMPTED |
| cyclic lex-smallest | reuse same cyclic axes with `+e` if both signs | lex-smallest reverse HOLDs with `+1,+1`; this reverse fails | ATTEMPTED |
| nm2ax axis-cover | reuse cover reverse hold | cover HOLDs reverse without cyclic signed columns; cover reverse HOLDs while this reverse fails | ATTEMPTED |
| nm2ax12 1-in 2-out split | reuse split reverse hold | split HOLDs reverse without the four-edge product; Cover and split do not score handedness; split reverse HOLDs while this reverse fails | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails coincidentally; leftover-empty is empty leftover of the union, not own-square holonomy fail at `S(A)` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and at `B` is `{e_2,e_3}`, nonempty equal; leftover of `M` reverse HOLDs while this reverse fails | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and at `B` is `{e_1}`, nonempty equal; leftover of `O` reverse HOLDs while this reverse fails | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold of `M` and of `O` | exist-opposite reverse of signed `M` HOLDs and exist-opposite reverse of signed `O` HOLDs while this reverse fails | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence fails at `A` and at `B` without cyclic columns | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-largest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(C,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient at `C` is `+1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | unsigned `Orient(A)=−1` while this Orient at `A` is `+1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(D)=3` | different seed; second pair is a new seed, not a formed child; here `t(A)=0` and `t(D)=2` | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe Orient reverse fails (`A` `−1`, `B` `+1`); this letter is the y-probe yz-plane unit square | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the y-probe yz-plane unit square | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-largest outgoing determinant orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face fail on the y-probe yz-plane unit squares | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is three disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(C)` sums to `0` while cyclic is `(−e_3,−e_1)` | ATTEMPTED |
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
missing identification of Orient with nm2oridetz unique signed `|O_i|=1`,
missing identification of Orient with nm2orichy leftover-axis, missing
identification of Orient with nm2orioney lex-one, missing identification of
Orient with cyclic lex-smallest, missing identification of Orient with
nmcover axis-cover, missing identification of Orient with nm2ax axis-cover,
missing identification of Orient with nm2ax12 1-in 2-out split, missing
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
Orient fail not `UNDEFINED`, four y-probes with seed `A`, `S(q)` the yz
unit square translated to first vertex `q`, square outside `B_3(0)` as fail
not `UNDEFINED`, second pair as a new seed not a formed child, third pair as
a new seed not a formed child, and mixed remains a set are declared. No
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
| per element | cyclic frame `F=(m,o_next,o_prev)` and signed-permutation sending around a yz unit square | no continuum alphabet |
| per site | four y-probe translates of the nm2holyzrd yz unit square on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four y-probe yz squares, holonomy, neighbor-read reverse/face | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for neighbor-read of
cyclic-frame holonomy reverse/face, a formation-rate rule, and a physical
selector among 1-in 2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Neighbor-read reverse fail and face fail are only leftover of
nm2yzrd3z untranslated yz neighbor-read, or of nm2yzrd3x x-probe yz
neighbor-read, or of nm2holyzrd two-axis yz neighbor-read, or of nm2holyz
yz-square holonomy, or of nm2sfzrdy neighbor-read of cyclic-frame
transport, or of nm2cycfrmz cyclic-frame transport, or of nm2oricyclz
cyclic Orient equal signs, or of neighbor-read of the scalar Orient sign,
or of cover and split; leftover-axis already answers reverse fail; lex-one
already answers reverse fail; unique signed `|O_i|=1` already answers mixed
`O`; leftover of `M` alone already answers reverse; leftover of `O` alone
already answers reverse; exist-opposite of signed `O` already answers
reverse; mixed #7188 already reported fail/fail; the second pair is only
the formed child `(0,0,1)` of the 1-axis seed; the third pair is only a
formed child of the two-axis seed; unique outgoing letters should be
required; cyclic lex-smallest already gives HOLD bits with opposite signs;
and unsigned incoming axis already gives the same signs because each `M`
letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Neighbor-read reverse fails because holonomy of `S(A)` fails
and holonomy of `S(B)` fails, not `UNDEFINED`. Neighbor-read face fails
because `S(C)` lies outside `B_3(0)` and holonomy of `S(D)` fails from
split fail at `D`. nm2yzrd3z reverse HOLDs on the untranslated `x=0`
square: leftover of that letter, not this reverse. The `−e_2` translate of
`S(A)` is that reverse square and has holonomy HOLD, so a mutation
ignoring holonomy at `S` would HOLD at `A`. nm2yzrd3x scores x-probe
translates whose `S(A)` is the face square and whose `S(C)` lies in
`B_3(0)`. nm2holyzrd scores the same untranslated yz squares on the
two-axis seed with `t(C)=2`. nm2holyz scores the product at `S` alone.
nm2sfzrdy reverse HOLDs from existential transport neighbor-read at `A`
and at `B`. Transport reverse HOLDs: leftover of nm2cycfrmz cyclic-frame
transport, not this holonomy. Scalar neighbor-read of Orient HOLDs at `A`
and at `B`; that is not the four-edge product. Unique nonnegative
permutation sending fails at `A` and at `B`. Cover and split HOLD reverse
on the y-probes and do not score the four-edge product. Leftover-axis
reverse fails because leftover-axis at `A` and at `B` fails. Lex-one
reverse fails from `e1<e2<e3` order independent of `m`. Lexicographic
unsigned `o1,o2` reverse fails with `−1,+1`. Unique signed `|O_i|=1`
reverse HOLDs coincidentally at `A` and at `B` while this reverse fails.
Cyclic lex-smallest reverse HOLDs with `+1,+1`. Presence of an opposite
pair in `O` fails at `A` and at `B`. Unique outgoing letters would assign
`UNDEFINED` at mixed `O(C)`; this Orient at `C` is `+1`, not `UNDEFINED`.
Leftover of `M` reverse HOLDs and leftover of `O` reverse HOLDs while this
reverse fails. Exist-opposite reverse of signed `M` HOLDs and of signed `O`
HOLDs while this reverse fails. Mixed #7188 is a different z-symmetric
process with mixed `M`. The second pair is a new seed, not a formed child:
`(0,0,1)` is recorded at tick 0 with lock `+e_2`, whereas the 1-axis child
forms at tick 1 with lock `+e_3`. The third pair is a new seed, not a formed
child: `(2,0,0)` is recorded at tick 0 with lock `+e_3`, whereas the
two-axis child at that site forms at tick 3 with lock `+e_1`. Reverse
neighbor-read is HOLD iff holonomy of `S(A)` HOLDs and some formed 6-NN
translate has holonomy HOLD, and likewise at `S(B)`, not leftover of
leftover-axis and not leftover of nm2orioney lex-one.

### N8 — cross-cycle echo

nm2yzrd3z neighbor-read of yz holonomy on this near-face seed reported
reverse hold and face fail on the untranslated `x=0` and `x=1` squares.
nm2holyzrd two-axis yz neighbor-read reported reverse hold and face fail
on the same two untranslated yz squares with four tick-0 seeds, `t(C)=2`,
and split fail at both `C` and `C1`. nm2sfzrdy neighbor-read of
cyclic-frame transport on these same y-probes reported reverse hold and
face fail. nm2ax cover on this seed reports cover HOLD reverse and cover
fail face. nm2ax12 1-in 2-out split likewise HOLDs reverse and fails face.
nm2chiraly lexicographic unsigned `o1,o2` on this seed reports unsigned
reverse fail. nm2oridetz unique signed outgoing letters on this seed
reports unique signed reverse HOLD coincidentally. nm2orichy leftover-axis
on this seed reports leftover reverse fail because leftover-axis at `A`
fails. nm2orioney lex-one reports lex-one reverse fail. Leftover axis
reports empty leftover at each of four y-probes, leftover reverse fail,
and leftover face fail. nm2oricyclz cyclic next/prev lex-largest Orient on
these y-probes reports Orient reverse hold. This note is not those
displays: it reports neighbor-read of cyclic-frame holonomy of
`(m,o_next,o_prev)` of `M` and `O` at `τ=t+1` around the four y-probe
yz-plane unit squares on the three-axis far-face opposite seed, with
`t(A)=0`, `t(B)=1`, `t(C)=1`, and `t(D)=2`, reverse neighbor-read fail, and
face neighbor-read fail, while nm2yzrd3z untranslated yz neighbor-read
reverse HOLDs and face fails, while nm2yzrd3x x-probe reverse fails and
face fails on different squares, while nm2holyzrd two-axis yz neighbor-read
reverse HOLDs and face fails from empty cyclic slots, while nm2holyz
yz-square holonomy reverse HOLDs and face fails from the product at `S`
alone, while nm2sfzrdy transport neighbor-read reverse HOLDs and face
fails, while nm2cycfrmz transport reverse HOLDs. Cover and split do not
score handedness.

**Gate disposition:** PASS for the neighbor-read cyclic-frame-holonomy
`t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the predicate
equals the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals nm2chiraly lexicographic unsigned `o1,o2`
HOLD,” “the predicate equals nm2oridetz unique signed HOLD,” “the
predicate equals nm2orichy leftover-axis HOLD,” “the predicate equals
nm2orioney lex-one HOLD,” “the predicate equals cyclic lex-smallest HOLD,”
“the predicate equals nm2oricyclz cyclic Orient HOLD,” “the predicate
equals nm2cycfrmz cyclic-frame transport HOLD,” “the predicate equals
nm2sfzrdy neighbor-read of cyclic-frame transport HOLD,” “the predicate
equals nm2holyzrd two-axis yz neighbor-read HOLD,” “the predicate equals
nm2yzrd3z neighbor-read of yz holonomy HOLD,” “the predicate equals
nm2yzrd3x x-probe yz neighbor-read HOLD,” “the predicate equals
nm2holyz yz-square holonomy HOLD,” “the predicate equals
scalar neighbor-read of Orient HOLD,” “the predicate equals unique
nonnegative permutation sending HOLD,” “the predicate equals nmcover
axis-cover HOLD,” “the predicate equals nm2ax axis-cover HOLD,” “the
predicate equals nm2ax12 1-in 2-out split HOLD,” “the predicate equals
the 1-axis opposite two-site seed,” “the predicate equals nmunopp union,”
“bits are Admissibility,” “split fail is UNDEFINED,” or “empty `O_i` is
UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis opposite
near-face perp-step incoming-lock process, reads each y-probe's own earliest
incoming set and own outgoing dual from the record prefix at that probe's
`t+1`, reports split of the pair, reports the cyclic frame
`F=(m,o_next,o_prev)` as nm2cycfrmhol, reports Orient as nm2oricyclz
lex-largest cyclic, reports `S(q)` as the yz unit square of nm2holyzrd
translated so its first vertex is the probe, reports holonomy of those
squares, reports neighbor-read of those squares from formed 6-NN
translates, lists new records
in `B_3(0)` between `t` and `t+1` that meet a probe's six-neighbors, and
checks Theorems 1--3. It also
checks that reverse neighbor-read fails and face neighbor-read fails, that
holonomy of each y-probe square fails, that `S(C)` lies outside `B_3(0)`
as fail not `UNDEFINED`, that a vertex outside `B_3(0)` is fail not
`UNDEFINED`, that nm2yzrd3z untranslated yz neighbor-read reverse HOLDs
and face fails, that a mutation ignoring holonomy at `S(A)` would HOLD at
`A` from the `−e_2` translate, that nm2yzrd3x x-probe squares fail reverse
and face with `S(C)` in host, that nm2holyzrd two-axis yz neighbor-read
reverse HOLDs and face fails, that nm2sfzrdy transport neighbor-read
reverse HOLDs and face fails, that nm2cycfrmz transport reverse HOLDs
while holonomy reverse fails, that scalar neighbor-read reverse HOLDs
while this reverse fails, that unique nonnegative permutation sending
fails at `A` and at `B`, that leftover-axis reverse fails because leftover-axis
at `A` fails and lex-one reverse fails from `e1<e2<e3`
order independent of `m`, that split fail is holonomy fail not
`UNDEFINED`, that empty `O_next` or empty `O_prev` is Orient fail not
`UNDEFINED`, that the 1-axis opposite two-site seed is a different member
with `t(D)=3`, that #7477 same-lock is a different member with `t(D)=3`,
that LIVE three-axis as a three-site seed is a different member, that leftover-empty fail is a different predicate,
that leftover of `M` alone and leftover of `O` alone are different objects,
that mixed sets remain sets, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
that the second pair is a new seed not a formed child, that the z-probes
and x-probes of this seed are not this letter, and that the display is not
the two-tick lock-count clock composition. No runner cache is written.
