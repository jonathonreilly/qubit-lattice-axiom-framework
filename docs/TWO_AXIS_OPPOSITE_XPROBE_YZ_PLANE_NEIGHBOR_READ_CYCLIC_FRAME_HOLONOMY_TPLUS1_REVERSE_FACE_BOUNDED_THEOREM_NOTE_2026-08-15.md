---
claim_id: two_axis_opposite_xprobe_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of yz-plane cyclic-frame holonomy at t+1 on the four x-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_xprobe_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Yz-Plane Cyclic-Frame Holonomy At t+1 Reverse And Face On Four X-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of cyclic-frame holonomy around the yz-plane unit
square `S(q)` with a vertex at each of the four x-probes at that probe's
`τ=t+1`, and reverse/face from that neighbor-read, on the two-axis
opposite seed in `B_3(0)={n:n·n<=9}`. Same process and x-probes as
nm2axx / nm2frmrdx. `F` and Orient as nm2cycfrmhol. Holonomy and
neighbor-read as nm2holyzrd. For each probe `q`, `S(q)` is the yz unit
square with a vertex at `q` as the SW corner
`(q, q+e_2, q+e_2+e_3, q+e_3)` lying in `B_3(0)`; else fail, not
`UNDEFINED`. Reverse `A,B`. Face `C,D`. Face is displayed, not adopted.
Let `t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)`
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
`u→v` of a formed six-neighbor pair on `S(q)`, `P(u,v)` is the unique 3×3
signed permutation with `det = Orient(u)Orient(v)` sending columns of
`F(u)` to columns of `F(v)`; if none, that edge fails. Holonomy of `S(q)`
is the matrix product `P12 P23 P34 P41`. Holonomy HOLDs if and only if
every vertex split HOLDs, every Orient is `±1`, every edge has `P`, and
the product is the 3×3 identity. Neighbor-read HOLDs at `S(q)` if and
only if holonomy(`S(q)`) HOLDs and some formed 6-NN translate of `S(q)`
(shift by one lattice unit in `B_3(0)`) has holonomy HOLD. If holonomy
fails at `S(q)`, neighbor-read fails, not `UNDEFINED`. Reverse HOLDs if
and only if neighbor-read of `S(A)` and of `S(B)` HOLD. Face HOLDs if and
only if neighbor-read of `S(C)` and of `S(D)` HOLD. Cover and split do
not score handedness. This is not leftover of nm2holyzrd neighbor-read of
yz-plane holonomy reverse HOLD face fail: that reverse HOLDs on the `x=0`
yz square `A-D-B-E` of four seeds, while none of these four x-probes is a
vertex of that HOLDING square; `S(A)` is that note's face square
`C-C1-C2-C3` whose holonomy fails. This is not leftover of LIVE y-probe
nm2yzrdy: those y-probes are `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`; `S` of y-probe `C` leaves `B_3(0)`, while `S(C)` of this
x-probe `C=(2,0,0)` lies in `B_3(0)` and still fails holonomy from split
fail. This is not leftover of nm2frmrdx neighbor-read of cyclic-frame
transport reverse fail face fail: transport HOLDs at `B` and at `C` while
neighbor-read of holonomy of `S(B)` and of `S(C)` fails. This is not
leftover of nm2cycfrmz cyclic-frame transport reverse HOLD face HOLD on
the z-probes. This is not leftover of nm2axx axis-cover. This is not
leftover of nm2ax12x 1-in 2-out split. This is not leftover of scalar
neighbor-read of Orient. This is not leftover of a unique nonnegative
permutation sending. This is not leftover of nm2oricyclz cyclic Orient.
This is not leftover of nm2orichz leftover-axis. This is not leftover of
nm2orionez lex-one. This is not leftover of nm2chiralz lexicographic
unsigned `o1,o2` orientation. This is not leftover of nm2oridetz unique
signed outgoing letters. This is not leftover of leftover-of-`M` alone.
This is not leftover of leftover-of-`O` alone. This is not leftover-empty
fail of leftover axis. This is not leftover of nmunopp union. This is
not leftover of nmt2opp `M` frozen at `t`. This is not leftover of
nmot2opp two-tick composition. This is not leftover of nmoutopp untimed
eventual-`O`. This is not leftover of mixed #7188 fail/fail. This is not
leftover of the 1-axis opposite two-site seed. This is not leftover of
the same-lock two-site seed. The second pair is a new seed, not a formed
child. `A` is not a seed. Uniqueness is not required. Mixed remains a
set. Displayed, not adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_xprobe_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_xprobe_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py)

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
lex-largest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m` and the
lex-largest signed outgoing letter on the cyclic next and prev axes of
`Axis(M)` under `+e < −e`. When split HOLDs, `F=(m,o_next,o_prev)` is
that LIVE three-axis frame. For a formed six-neighbor edge of `S(q)`, `P`
is the unique signed permutation sending columns of `F(u)` to columns of
`F(v)` with determinant `Orient(u)Orient(v)`. Holonomy is the product of
the four edge matrices around `S(q)`. Neighbor-read of that holonomy HOLDs
at `S(q)` if and only if holonomy of `S(q)` HOLDs and some formed 6-NN
translate in `B_3(0)` also has holonomy HOLD. Reverse and face are scored
on neighbor-read HOLD of `S(A)` and `S(B)`, and of `S(C)` and `S(D)`.
Holonomy of nm2holyzrd on the `x=0` reverse square is a different readout:
that reverse HOLDs. Neighbor-read of cyclic-frame transport of nm2frmrdx
is a different readout: it is existential at a probe, not the product
around `S(q)`. Neighbor-read of the scalar Orient sign is a different
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
claim_type_reason: "Exact report of neighbor-read of cyclic-frame holonomy around the yz-plane unit square S(q) of M and O at t+1 on the four x-probes of the two-axis opposite seed, F and Orient at the probes and at the square vertices, P on each edge, holonomy matrices, neighbor-read of those squares, reverse fail and face fail from neighbor-read of S(A),S(B) and S(C),S(D); uniqueness of a sending is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_xprobe_yz_plane_neighbor_read_cyclic_frame_holonomy_tplus1_reverse_face
target_blocker_text: "display neighbor-read of yz-plane cyclic-frame holonomy reverse/face on the four x-probes of the two-axis opposite seed, not nm2holyzrd yz-square reverse HOLD, not LIVE y-probe nm2yzrdy, not nm2frmrdx transport neighbor-read, not nm2cycfrmz transport, not scalar neighbor-read of Orient, not unique nonnegative sending, not leftover-axis, not lex-one e1<e2<e3, not unique |O_i|=1, not unsigned axis units, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of cyclic-frame holonomy of F around S(q) at t+1 on the four x-probes displayed; do not write holonomy into Admissibility, do not reduce to nm2holyzrd yz-square reverse HOLD, do not reduce to LIVE y-probe nm2yzrdy, do not reduce to nm2frmrdx transport, do not reduce to nm2cycfrmz transport, do not reduce to scalar neighbor-read of Orient, do not reduce to unique nonnegative permutation sending, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-smallest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace holonomy by unique outgoing letters, do not replace holonomy by existential opposite of signed locks, do not replace holonomy by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of cyclic-frame holonomy around the yz-plane unit square S(q) of M and O at t+1 on the four x-probes of the two-axis opposite seed and reverse/face from that neighbor-read; displayed, not adopted"
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
yz-plane unit square `S(q)` has neighbor-read of cyclic-frame holonomy of
`F=(m,o_next,o_prev)` of `M` and `O` scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is not a seed. Same process and x-probes as nm2axx.

For each probe `q`, `S(q)` is the yz unit square with a vertex at `q`:

```text
S(q) = (q, q+e_2, q+e_2+e_3, q+e_3).
```

A vertex of `S(q)` outside `B_3(0)` is fail, not `UNDEFINED`. These squares
are not the nm2holyzrd reverse yz square `A=(0,0,0)`, `D=(0,1,0)`,
`B=(0,1,1)`, `E=(0,0,1)` at `x=0`. `S(A)` coincides with that note's face
square at `x=1`.

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

## Named neighbor-read of yz-plane cyclic-frame holonomy of `(m,o_next,o_prev)` at `τ=t+1`

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
Order +e < −e. o_next is lex-largest in O_next (hence −e if both signs).
o_prev likewise.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

When split HOLDs, `F(q)=(m, o_next, o_prev)`. For an edge `u→v` of a formed
six-neighbor pair on `S(q)`:

```text
P(u,v) is the unique 3×3 signed permutation with
det(P)=Orient(u)Orient(v) sending columns of F(u) to columns of F(v).
If none, that edge fails, not UNDEFINED.
Holonomy(S(q)) HOLDs iff every vertex of S(q) is in B_3(0), every
vertex split HOLDs, every Orient is ±1, every edge has P, and
P12 P23 P34 P41 is the 3×3 identity.
If any vertex of S(q) lies outside B_3(0), holonomy fails, not UNDEFINED.
Neighbor-read HOLDs at S(q) iff holonomy(S(q)) HOLDs and some formed
6-NN translate of S(q) in B_3(0) has holonomy HOLD.
If holonomy fails at S(q), neighbor-read fails, not UNDEFINED.
Uniqueness of a translate is not required.
```

Reverse neighbor-read of cyclic-frame holonomy holds if and only if
neighbor-read HOLDs at `S(A)` and at `S(B)`. Face neighbor-read of
cyclic-frame holonomy holds if and only if neighbor-read HOLDs at `S(C)`
and at `S(D)`. Either side `UNDEFINED` is `UNDEFINED`. Else if both sides
HOLD, reverse or face HOLDs. Else fail.

Cover and split do not score handedness. Identifying nm2holyzrd reverse
HOLD with this reverse is refused: that reverse HOLDs on the `x=0` yz
square of four seeds; this reverse fails because `S(A)` and `S(B)` have
holonomy fail. Identifying LIVE y-probe nm2yzrdy with this reverse is
refused: y-probe `C=(0,2,0)` has `S` leaving `B_3(0)`, while this
x-probe `C` has `S(C)` in `B_3(0)`. Identifying nm2frmrdx transport
neighbor-read with this reverse is refused: transport HOLDs at `B` and at
`C` while holonomy neighbor-read fails there. Identifying nm2cycfrmz
z-probe transport reverse HOLD and face HOLD with this reverse is refused.
Identifying leftover-empty fail with this reverse is refused: leftover is
empty at `B` while this reverse fails because holonomy of `S(A)` and of
`S(B)` fails. Identifying scalar neighbor-read of Orient with this reverse
is refused. Identifying a unique nonnegative permutation sending with this
reverse is refused.

## Theorem 1 — ticks, squares, holonomy, neighbor-read at `A,B,C,D`

On this process the four x-probes form in `B_3(0)`. Compare to nm2holyzrd:
neighbor-read of the `x=0` yz square HOLDs and neighbor-read of the `x=1`
face square fails; this letter scores `S(q)` at each x-probe, reverse fails,
and face fails. Compare to LIVE y-probe nm2yzrdy: those probes are not these
x-probes; `S` of y-probe `C` leaves `B_3(0)`. Compare to nm2frmrdx: transport
neighbor-read HOLDs at `B` and at `C`. Compare to nm2axx cover and nm2ax12x
split: both fail reverse and fail face on these x-probes without a four-edge
product. Compare to nm2cycfrmz: z-probe transport reverse HOLDs and face
HOLDs. Compare to scalar neighbor-read of Orient: fail at each of the four
x-probes. This display reads neighbor-read of cyclic-frame holonomy of
`(m,o_next,o_prev)` around `S(q)` of those same timed sets:

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
O(D, τ) = {+e_1, −e_1}
split(A) = fail
split(B) = hold
split(C) = hold
split(D) = fail
m(A) = −e_3
i(A) = 3
o_next(A) fail
o_prev(A) fail
det(A) = fail
Orient(A) = fail
m(B) = +e_1
i(B) = 1
o_next(B) = +e_2
o_prev(B) = −e_3
det(B) = -1
Orient(B) = −1
m(C) = +e_1
i(C) = 1
o_next(C) = −e_2
o_prev(C) = −e_3
det(C) = 1
Orient(C) = +1
m(D) = −e_3
i(D) = 3
o_next(D) fail
o_prev(D) fail
det(D) = fail
Orient(D) = fail
F(A) = fail
F(B) = (+e_1, +e_2, −e_3)
F(C) = (+e_1, −e_2, −e_3)
F(D) = fail
S(A) = ((1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1))
S(B) = ((1, 1, 1), (1, 2, 1), (1, 2, 2), (1, 1, 2))
S(C) = ((2, 0, 0), (2, 1, 0), (2, 1, 1), (2, 0, 1))
S(D) = ((1, 1, 0), (1, 2, 0), (1, 2, 1), (1, 1, 1))
split(S(A)_0) = fail
split(S(A)_1) = fail
split(S(A)_2) = hold
split(S(A)_3) = hold
P(S(A)_0→S(A)_1) = fail
P(S(A)_1→S(A)_2) = fail
P(S(A)_2→S(A)_3) = [1 0 0; 0 -1 0; 0 0 1]
P(S(A)_3→S(A)_0) = fail
holonomy(S(A)) = fail
holonomy(S(B)) = fail
holonomy(S(C)) = fail
holonomy(S(D)) = fail
holonomy(S(A) + e_1) = fail
holonomy(S(A) − e_1) = hold
holonomy(S(A) + e_2) = fail
holonomy(S(A) − e_2) = fail
holonomy(S(A) + e_3) = fail
holonomy(S(A) − e_3) = fail
neighbor-read(S(A)) = fail
neighbor-read(S(B)) = fail
neighbor-read(S(C)) = fail
neighbor-read(S(D)) = fail
```

`A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with
incoming `{−e_3}`. Mixed remains a set: `O(B,τ)` has three outgoing
steps, `O(C,τ)` has three outgoing steps, and `O(D,τ)` has two outgoing
steps on one axis. Unique outgoing letters would assign `UNDEFINED` at
those mixed outgoing sets. Unique signed `|O_i|=1` fails at `B` and at
`C` because those outgoing sets have an opposite pair. Lex-largest picks
`−e` on each mixed cyclic slot, so `(o_next,o_prev)` is defined at `B`
and at `C`. `M` is a singleton at each probe, so the unique signed `m`
exists. Split fails at `A` and at `D` because cover fails:
`Axis(M)∪Axis(O)={e_1,e_3}` misses `e_2`. Split HOLDs at `B` and at `C`.
Cover and split do not score that cyclic lex-largest Orient is
`fail,−1,+1,fail`, and they do not score the four-edge product around
`S(q)`. At `A`, `i=3` so `e_next=e_1` and `e_prev=e_2`; `O_prev` is empty,
so Orient fails, not UNDEFINED. At `D`, `i=3` and `O={±e_1}` likewise has
empty `O_prev`. At `B`, `i=1` so `e_next=e_2` and `e_prev=e_3`; mixed
`O_prev={±e_3}` yields `o_prev=−e_3`. At `C`, `i=1` and mixed
`O_prev={±e_3}` yields `o_prev=−e_3` with `o_next=−e_2`. O is not M.

`S(A)` is exactly the nm2holyzrd face square `C-C1-C2-C3`. Holonomy of
`S(A)` fails because `S(A)_0=(1,0,0)` and `S(A)_1=(1,1,0)` are split fail
(empty cyclic outgoing slot), so neighbor-read of `S(A)` fails, not
`UNDEFINED`, even though holonomy of the `−e_1` translate
`holonomy(S(A) − e_1) = hold` (that translate is the nm2holyzrd reverse
square). `S(B)` fails from split fail at `(1,2,2)` and at `(1,1,2)`.
`S(C)` fails from split fail at `(2,1,1)` and at `(2,0,1)`. `S(D)` fails
from split fail at `(1,1,0)` and at `(1,2,0)`. A vertex outside `B_3(0)`
is fail, not `UNDEFINED`.

On the 1-axis opposite two-site seed, `t(A)=3` and `t(C)=4`. That is
leftover of the first pair. Here both `(0,0,1)` and `(0,1,1)` are seeds of
a second opposite pair on a second axis. On the y-probes of this same
seed, y-probe `A` is a seed at tick 0 and `S` of y-probe `C` leaves
`B_3(0)`. On the z-probes of this same seed, transport reverse HOLDs and
transport face HOLDs. Those probe-direction readouts are not this x-probe
display.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at `A`, `B`, and
`C`, and `O(D,t)={−e_1}`. Split fails, Orient is fail, not UNDEFINED, and
the cyclic frame fails, not UNDEFINED, at each probe at `t`. Holonomy of
`S(q)` at a cut with empty `O` therefore fails, not UNDEFINED.

Transport HOLDs at `B` and at `C`. Transport fails at `A` and at `D`
because split fails. Neighbor-read of holonomy of `S(q)` fails at each of
the four x-probes because holonomy of each `S(q)` fails, not `UNDEFINED`.
Uniqueness of a matching neighbor is not required. Scalar neighbor-read
fails at each of the four x-probes. Unique nonnegative permutation sending
fails at each probe. The 3-split is a field: opposite Orient at a neighbor
is allowed when `det(P)` equals the product of the two signs. This is not
leftover of nm2holyzrd: that reverse HOLDs. This is not leftover of LIVE
y-probe nm2yzrdy. This is not leftover of nm2frmrdx: transport HOLDs at
`B` and at `C`.

## Theorem 2 — reverse from neighbor-read of cyclic-frame holonomy at `τ`

Reverse neighbor-read of cyclic-frame holonomy holds if and only if
neighbor-read HOLDs at `S(A)` and at `S(B)`. `neighbor-read(S(A))=fail`
and `neighbor-read(S(B))=fail`. Reverse fails. This is HOLD iff both
neighbor-reads HOLD, not leftover of nm2holyzrd yz-square reverse HOLD,
not leftover of LIVE y-probe nm2yzrdy, not leftover of nm2frmrdx
transport neighbor-read, not leftover of nm2cycfrmz cyclic-frame
transport sending, not leftover of nm2oricyclz cyclic Orient equal signs,
not leftover of scalar neighbor-read, not leftover of a unique
nonnegative permutation sending, not leftover of nm2chiralz lexicographic
unsigned `o1,o2`, not leftover of nm2oridetz unique signed outgoing
letters, not leftover of nm2orichz leftover-axis, not leftover of
nm2orionez lex-one, not leftover of nm2axx axis-cover, not leftover of
nm2ax12x 1-in 2-out split, not leftover-empty fail, and not exist-opposite.

Reverse neighbor-read cyclic-frame holonomy at τ: fail

Both sides are defined, so this is not `UNDEFINED`. nm2holyzrd reverse
HOLDs on the `x=0` yz square; this reverse fails. Transport HOLDs at `B`
while holonomy neighbor-read of `S(B)` fails. Cover reverse fails because
cover fails at `A` and HOLDs at `B`. Split reverse fails because split
fails at `A` and HOLDs at `B`. Cover and split do not score handedness.

## Theorem 3 — face from neighbor-read of cyclic-frame holonomy at `τ`

Face neighbor-read of cyclic-frame holonomy holds if and only if
neighbor-read HOLDs at `S(C)` and at `S(D)`. `neighbor-read(S(C))=fail`
and `neighbor-read(S(D))=fail`. Face fails. Face is displayed, not
adopted. This is HOLD iff both neighbor-reads HOLD, not leftover of
nm2holyzrd face fail on the same `x=1` square as `S(A)` while this face
also uses `S(C)` at `x=2`, not leftover of LIVE y-probe nm2yzrdy whose
`S(C)` leaves `B_3(0)` while this `S(C)` lies in `B_3(0)`, not leftover
of nm2frmrdx whose transport HOLDs at `C`, not leftover of nm2cycfrmz
z-probe face HOLD, not leftover of scalar neighbor-read, not leftover of
a unique nonnegative permutation sending, not leftover of nm2axx
axis-cover, not leftover of nm2ax12x 1-in 2-out split, not leftover-empty
fail, and not exist-opposite.

Face neighbor-read cyclic-frame holonomy at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Transport HOLDs at `C`
while holonomy neighbor-read of `S(C)` fails. Pair-presence of an opposite
pair in `O` HOLDs at `C` and at `D` while this face fails. A vertex
outside `B_3(0)` is fail, not `UNDEFINED`.

## What this note does not claim

- It does not replace neighbor-read by nm2holyzrd yz-square reverse HOLD.
- It does not replace this letter by LIVE y-probe nm2yzrdy.
- It does not replace holonomy by nm2frmrdx neighbor-read of cyclic-frame transport.
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
- It does not reprint nm2axx axis-cover reverse fail face fail as this
  oriented display.
- It does not reprint nm2ax12x 1-in 2-out split reverse fail face fail as
  this oriented display.
- It does not reprint nm2chiralz lexicographic unsigned `o1,o2`.
- It does not reprint nm2oridetz unique signed reverse fail face fail as
  this oriented display.
- It does not reprint nm2orichz leftover-axis.
- It does not reprint nm2orionez lex-one.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not score the y-probes or the z-probes as this letter.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this oriented display.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint the two-tick lock-count clock composition. This is not the two-tick lock-count clock composition.
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

This display uses Lattice to name `B_3(0)` and the four x-probe squares. It
uses Qubit only as the algebra of the local possibility domain. It uses
Record only as a boundary: a present lock is content. It does not rewrite
Admissibility. The two-axis opposite seed process, neighbor-read of
cyclic-frame holonomy of `(m,o_next,o_prev)` of `M` and `O` at `t+1`
around `S(q)`, and the reverse/face bits from that neighbor-read are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `S(q)` yz unit square with a vertex at each x-probe | Theorem 1; SW corner; in `B_3(0)` at all four x-probes |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual at `B,C`; singleton at `A`; mixed pair at `D` |
| split at `τ` | Theorem 1; fail at `A,D`; HOLD at `B,C` |
| unique signed `m`, axis index `i`, cyclic `(o_next,o_prev)` | Theorem 1; singleton `M`; cyclic pair defined at `B,C`; empty `O_prev` fail at `A,D` |
| integer `det(m,o_next,o_prev)` | Theorem 1; fail, `-1`, `1`, fail |
| Orient at `τ` | Theorem 1; fail, `−1`, `+1`, fail |
| cyclic frame `F=(m,o_next,o_prev)` | Theorem 1; fail at `A,D`; LIVE three-axis at `B,C` |
| holonomy of `S(A)`, `S(B)`, `S(C)`, `S(D)` | Theorem 1; fail, fail, fail, fail |
| neighbor-read of those squares | Theorem 1; fail, fail, fail, fail; `S(A)−e_1` holonomy hold |
| leftover of nm2holyzrd yz-square reverse HOLD | Theorem 1; that reverse HOLDs on `x=0`; this reverse fails |
| leftover of LIVE y-probe nm2yzrdy | Theorem 1; y-probe `C` square leaves the host |
| leftover of nm2frmrdx transport neighbor-read | Theorem 1; transport HOLDs at `B,C` |
| leftover of nm2cycfrmz cyclic-frame transport | Theorem 1; z-probe transport reverse hold and face hold |
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
| leftover of nm2axx axis-cover | not this oriented display |
| leftover of nm2ax12x 1-in 2-out split | not this oriented display |
| leftover of nm2chiralz lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichz leftover-axis | not this oriented display |
| leftover of nm2orionez lex-one signed `e1<e2<e3` | not this oriented display |
| leftover of cyclic lex-smallest | not this oriented display |
| leftover of nm2oricyclz cyclic Orient equal signs | not this holonomy |
| leftover of nm2cycfrmz cyclic-frame transport | not this holonomy |
| leftover of nm2holyzrd yz-square holonomy reverse HOLD | not this x-probe scoring |
| leftover of LIVE y-probe nm2yzrdy | not this x-probe scoring |
| leftover of scalar neighbor-read of Orient | not this holonomy |
| leftover of unique nonnegative permutation sending | not this holonomy |
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
| leftover of the 1-axis opposite two-site seed | not this display |
| leftover of the same-lock two-site seed | not this display |
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
| V1 | It answers the first-display question: neighbor-read of cyclic-frame holonomy around the yz-plane unit square `S(q)` of `(m,o_next,o_prev)` of `M` and `O` at `t+1` on the four x-probes of the two-axis opposite seed, and reverse/face from that neighbor-read. |
| V2 | Current main has no landed neighbor-read of yz-plane cyclic-frame-holonomy reverse/face of timed `M` and `O` on these four x-probes of the two-axis opposite seed. |
| V3 | Squares, holonomy matrices, neighbor-read of those squares, and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the four-edge product around `S(q)` and a formed 6-NN translate, reverse fails and face fails while nm2holyzrd reverse HOLDs on the `x=0` square, while nm2frmrdx transport HOLDs at `B` and at `C`, and while LIVE y-probe `S(C)` leaves the host. |
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
nmcover axis-cover, does not replace Orient by nm2axx axis-cover, does not
replace Orient by nm2ax12x 1-in 2-out split, does not identify this
display with the 1-axis opposite two-site seed, and does not identify it
with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2holyzrd yz-square neighbor-read | reuse reverse HOLD on `A-D-B-E` at `x=0` | that reverse HOLDs; this reverse fails; no x-probe is a vertex of the HOLDING square; `S(A)` is that note's failing face square | ATTEMPTED |
| LIVE y-probe nm2yzrdy | score the four y-probes | y-probes are `(0,1,0),(1,1,1),(0,2,0),(1,1,0)`; `S` of y-probe `C` leaves `B_3(0)` while `S(C)` here is in the host | ATTEMPTED |
| nm2frmrdx transport neighbor-read | reuse transport HOLD bits at the x-probes | transport HOLDs at `B` and at `C` while holonomy neighbor-read fails there; reverse/face bits agree fail/fail but the per-probe objects differ | ATTEMPTED |
| nm2cycfrmz cyclic-frame transport | reuse z-probe reverse HOLD and face HOLD | z-probe transport reverse HOLDs and face HOLDs; this letter is holonomy of `S(q)` on x-probes | ATTEMPTED |
| scalar neighbor-read of Orient | reuse equal Orient sign at some formed 6-NN | scalar fails at each of `A,B,C,D`; this object is the four-edge product | ATTEMPTED |
| unique nonnegative permutation sending | require a unique sending with no minus signs | unique nonnegative sending fails at each of `A,B,C,D`; uniqueness is not required | ATTEMPTED |
| nm2oricyclz cyclic Orient | reuse Orient reverse hold and face hold from equal `±1` signs | Orient reverse HOLDs and face HOLDs on the z-probes without a four-edge product; this x-probe reverse fails | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face hold | lex-one at `B` is `+1` while cyclic Orient at `B` is `−1`; unsigned columns are not cyclic `o_next,o_prev` | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed fails at `B` and at `C` while split HOLDs there; an opposite pair in `O` makes `|O_i|≠1` but lex-largest still picks `−e` | ATTEMPTED |
| nm2orichz leftover-axis | reuse leftover-axis reverse hold and face fail | leftover-axis at `B` and at `C` is `−1,−1` without a four-edge product | ATTEMPTED |
| nm2orionez lex-one | reuse lex-one reverse fail and face hold | lex-one at `B` is `+1` from `e1<e2<e3` order independent of `m`; cyclic Orient at `B` is `−1` | ATTEMPTED |
| cyclic lex-smallest | reuse same cyclic axes with `+e` if both signs | lex-smallest at `B` is `+1` while cyclic lex-largest at `B` is `−1` | ATTEMPTED |
| nm2axx axis-cover | reuse cover reverse fail and cover face fail on these x-probes | cover fails reverse and face without cyclic signed columns or a four-edge product | ATTEMPTED |
| nm2ax12x 1-in 2-out split | reuse split reverse fail and split face fail | `|Axis(M)|=1` at each probe so split equals cover; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails from empty leftover at `B`; this reverse fails because holonomy of `S(A)` and of `S(B)` fails | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_2}` and at `B` is `{e_2,e_3}`, nonempty unequal | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2,e_3}` and at `B` is `{e_1}`, nonempty unequal | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `M` and of signed `O` both fail on these x-probes; that readout never reads the product | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence fails at `A` and HOLDs at `B,C,D`; pair-presence face HOLDs while this face fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; holonomy is a four-edge product | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(B,τ)` remains a set; unique-letter Orient at `B` is `UNDEFINED` while this Orient is `−1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member both agree at `B` and at `C`; flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_prev` at `A` and at `D` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=3`, `t(C)=4` | different seed; second pair is a new seed, not a formed child; here `t(A)=2` | ATTEMPTED |
| y-probe neighbor-read | score the four y-probes on this seed | y-probe `S(C)` leaves `B_3(0)`; this letter is the four x-probes | ATTEMPTED |
| z-probe neighbor-read | score the four z-probes on this seed | z-probe transport reverse HOLDs and z-face HOLDs; this letter is the four x-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores holonomy of `S(q)` at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face fail from holonomy fail of `S(q)` on the two-axis opposite seed | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is two disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(B)` sums to `+e_2` while cyclic is `(+e_2,−e_3)` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of this reverse with
nm2holyzrd reverse HOLD, missing identification with LIVE y-probe
nm2yzrdy, missing identification with nm2frmrdx transport HOLD at `B` and
at `C`, missing identification of Orient with leftover of `M` alone,
missing identification of Orient with leftover-empty fail, missing
identification of Orient with existential opposite of signed locks, missing
identification of Orient with presence of an opposite pair in `O`, missing
identification of Orient with nm2chiralz lexicographic unsigned `o1,o2`,
missing identification of Orient with nm2oridetz unique signed `|O_i|=1`,
missing identification of Orient with nm2orichz leftover-axis, missing
identification of Orient with nm2orionez lex-one, missing identification of
Orient with cyclic lex-smallest, missing identification of Orient with
nmcover axis-cover, missing identification of Orient with nm2axx axis-cover,
missing identification of Orient with nm2ax12x 1-in 2-out split, missing
identification of this seed with the 1-axis opposite two-site seed, and
missing Record identification of holonomy reverse are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
next/prev axes of `Axis(M)`, lex-largest signed outgoing letter under
`+e < −e` (hence `−e` if both signs), integer determinant sign, empty
`O_next` or empty `O_prev` as Orient fail not `UNDEFINED`, split fail as
Orient fail not `UNDEFINED`, `S(q)` the yz unit square with SW vertex at
the probe, vertex outside `B_3(0)` as fail not `UNDEFINED`, four x-probes
with `A` not a seed, second pair as a new seed not a formed child, and
mixed remains a set are declared. No uniqueness of outgoing locks, no
six-neighbor lock union as the scored object, no lock-count clock, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
holonomy `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | cyclic frame `F` and neighbor-read of four-edge holonomy of `S(q)` at `t+1` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | `S(q)`, edge sendings, holonomy, neighbor-read, reverse/face from neighbor-read | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for neighbor-read of
cyclic-frame holonomy reverse/face, a formation-rate rule, and a physical
selector among 1-in 2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Neighbor-read reverse fail and face fail are only leftover of
nm2holyzrd face fail, or of LIVE y-probe nm2yzrdy, or of nm2frmrdx
transport reverse fail face fail, or of nm2axx cover fail, or of nm2ax12x
split fail, or of leftover-empty fail; nm2holyzrd already answered reverse
HOLD on the yz square; nm2cycfrmz already answered reverse HOLD and face
HOLD on the z-probes of this seed; scalar neighbor-read already fails
reverse and face; unique signed `|O_i|=1` already answers mixed `O`;
leftover of `M` alone already answers reverse; leftover of `O` alone
already answers reverse; exist-opposite of signed `O` already answers
reverse; mixed #7188 already reported fail/fail; the second pair is only
the formed child `(0,0,1)` of the 1-axis seed; unique outgoing letters
should be required; cyclic lex-smallest already gives the same fail bits;
and unsigned incoming axis already gives the same signs because each `M`
letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores empty leftover at `B` as reverse fail.
Neighbor-read reverse fails because holonomy of `S(A)` and of `S(B)` fails.
Neighbor-read face fails because holonomy of `S(C)` and of `S(D)` fails.
nm2holyzrd reverse HOLDs on the `x=0` yz square of four seeds; none of
these x-probes is a vertex of that square. `S(A)` is that note's face
square, whose holonomy fails even though `holonomy(S(A) − e_1) = hold`.
LIVE y-probe nm2yzrdy uses `C=(0,2,0)` whose `S` leaves `B_3(0)`; this
`S(C)` lies in `B_3(0)`. nm2frmrdx transport HOLDs at `B` and at `C` while
holonomy neighbor-read fails there. Equal transport bits including
fail=fail are not this four-edge product. Scalar neighbor-read of Orient
fails at each of the four x-probes. Unique nonnegative permutation sending
fails at each probe. Cover and split fail reverse and face on this member
and do not score the four-edge product. Pair-presence face HOLDs while this
face fails. Unique signed `|O_i|=1` fails at `B` and at `C` while split
HOLDs there. Lex-one at `B` is `+1` while cyclic Orient at `B` is `−1`.
Cyclic lex-smallest at `B` is `+1`. Unique outgoing letters would assign
`UNDEFINED` at mixed `O(B)`; this Orient is `−1`, not `UNDEFINED`.
nm2cycfrmz on the four z-probes of this same seed reports reverse HOLD and
face HOLD; this letter is holonomy of `S(q)` on the four x-probes. Mixed
#7188 is a different z-symmetric process with mixed `M`. The second pair
is a new seed, not a formed child: `(0,0,1)` is recorded at tick 0 with
lock `+e_2`, whereas the 1-axis child forms at tick 1 with lock `+e_3`.
Reverse neighbor-read of cyclic-frame holonomy is HOLD iff neighbor-read
HOLDs at `S(A)` and at `S(B)`, not leftover of nm2holyzrd reverse HOLD
and not leftover of nm2frmrdx transport.

### N8 — cross-cycle echo

nm2axx cover on this two-axis seed reported cover fail at `A` and at `D`,
cover HOLD at `B` and at `C`, reverse fail, and face fail. nm2ax12x 1-in
2-out split on the same seed reported the same reverse fail and face fail
because `|Axis(M)|=1` at each x-probe. nm2frmrdx neighbor-read of
cyclic-frame transport on these same x-probes reported transport fail at
`A` and at `D`, HOLD at `B` and at `C`, reverse fail, and face fail.
nm2holyzrd neighbor-read of yz-plane holonomy on the two yz squares of
this same seed reported reverse hold and face fail. nm2cycfrmz
cyclic-frame transport on the four z-probes of this same seed reported
reverse hold and face hold. The four y-probes of this same seed are not
these x-probes; y-probe `A` is a seed at tick 0. Unique signed outgoing
letters fail at `B` and at `C`. Leftover axis on these x-probes is `{e_2}`
at `A` and at `D` and empty at `B` and at `C`. This note is not those
displays: it reports neighbor-read of yz-plane cyclic-frame holonomy of
`(m,o_next,o_prev)` of `M` and `O` at `τ=t+1` on the four x-probes of the
two-axis opposite seed, with `t(A)=2`, `t(B)=1`, `t(C)=3`, and `t(D)=2`,
`holonomy(S(A))=fail`, `holonomy(S(B))=fail`, `holonomy(S(C))=fail`,
`holonomy(S(D))=fail`, `neighbor-read(S(A))=fail`,
`neighbor-read(S(B))=fail`, `neighbor-read(S(C))=fail`,
`neighbor-read(S(D))=fail`, reverse fail, and face fail, while nm2holyzrd
reverse HOLDs, while nm2frmrdx transport HOLDs at `B` and at `C`, and
while LIVE y-probe `S(C)` leaves the host. Cover and split do not score
handedness.

**Gate disposition:** PASS for the neighbor-read of yz-plane
cyclic-frame-holonomy `t+1` reverse/face reports above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals six-neighbor lock union,”
“the predicate equals leftover-empty fail,” “the predicate equals leftover
of `M` alone,” “the predicate equals leftover of `O` alone,” “the predicate
equals exist-opposite HOLD,” “the predicate equals opposite-pair presence
in `O`,” “the predicate equals nm2chiralz lexicographic unsigned `o1,o2`
HOLD,” “the predicate equals nm2oridetz unique signed HOLD,” “the
predicate equals nm2orichz leftover-axis HOLD,” “the predicate equals
nm2orionez lex-one HOLD,” “the predicate equals cyclic lex-smallest HOLD,”
“the predicate equals nm2oricyclz cyclic Orient HOLD,” “the predicate
equals nm2cycfrmz cyclic-frame transport HOLD,” “the predicate equals
nm2frmrdx transport neighbor-read HOLD,” “the predicate equals nm2holyzrd
yz-square reverse HOLD,” “the predicate equals LIVE y-probe nm2yzrdy,”
“the predicate equals scalar neighbor-read of Orient HOLD,” “the predicate
equals unique nonnegative permutation sending HOLD,” “the predicate equals
nmcover axis-cover HOLD,” “the predicate equals nm2axx axis-cover HOLD,”
“the predicate equals nm2ax12x 1-in 2-out split HOLD,” “the predicate
equals the 1-axis opposite two-site seed,” “the predicate equals nmunopp
union,” “bits are Admissibility,” “split fail is UNDEFINED,” or “empty
`O_i` is UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each x-probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports split of the pair, reports the cyclic frame `F=(m,o_next,o_prev)`
as nm2cycfrmhol, reports Orient as nm2oricyclz lex-largest cyclic, builds
`S(q)` the yz unit square with a vertex at each x-probe, reports `P` on
each formed six-neighbor edge of `S(q)`, reports the holonomy products,
reports neighbor-read of those squares from formed 6-NN translates, lists
new records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that reverse
neighbor-read fails and face neighbor-read fails, that holonomy of each
`S(q)` fails, that a vertex outside `B_3(0)` is fail not `UNDEFINED`, that
nm2holyzrd reverse HOLDs on the `x=0` square while this reverse fails, that
LIVE y-probe `S(C)` leaves the host, that nm2frmrdx transport HOLDs at `B`
and at `C` while holonomy neighbor-read fails there, that nm2cycfrmz
transport reverse HOLDs and transport face HOLDs on the z-probes, that
scalar neighbor-read fails at each of `A,B,C,D`, that unique nonnegative
permutation sending fails at each of `A,B,C,D`, that split fail is
holonomy fail not `UNDEFINED`, that empty `O_next` or empty `O_prev` is
Orient fail not `UNDEFINED`, that the 1-axis opposite two-site seed is a
different member with `t(A)=3`, that same-lock is a different member with
`t(A)=3`, that LIVE three-axis as a three-site seed is a different member,
that leftover-empty fail is a different predicate, that leftover of `M`
alone and leftover of `O` alone are different objects, that mixed sets
remain sets, that the construction does not sum, that a formation member
from already-recorded six-neighbor locks is not attached, that the second
pair is a new seed not a formed child, that the y-probes and z-probes of
this seed are not this letter, and that the display is not the two-tick
lock-count clock composition. No runner cache is written.
