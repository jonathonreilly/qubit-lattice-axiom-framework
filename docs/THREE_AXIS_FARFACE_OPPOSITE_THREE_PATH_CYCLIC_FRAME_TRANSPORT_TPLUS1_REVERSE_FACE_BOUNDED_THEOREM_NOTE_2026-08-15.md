---
claim_id: three_axis_farface_opposite_three_path_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Equality of the three length-3 path-ordered products of cyclic-frame transport along the permutations of {e1,e2,e3} at t+1 on the three-axis far-face opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_farface_opposite_three_path_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Three-Path Cyclic-Frame Transport At t+1 Reverse And Face On The Three-Axis Far-Face Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** equality of the three length-3 path-ordered products of cyclic-frame
transport along the cyclic permutations of `{+e_1,+e_2,+e_3}` at each start's
`τ=t+1` on the three-axis far-face opposite seed in `B_3(0)={n:n·n<=9}`, and
reverse/face from that equality. `F` and Orient and `P` as nm2cycfrmhol.
Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)` and `(0,1,1)`.
For a start `s` let `w=s+e_1+e_2+e_3`. If `w·w>9`, the letter at `s` is fail,
not `UNDEFINED`. The three paths of length 3 from `s` to `w` are the
six-neighbor walks along the three cyclic permutations of
`(+e_1,+e_2,+e_3)`. A path exists iff every vertex is in `B_3(0)` and formed
at `τ` and every edge has a `P` as in nm2cycfrmhol. The path product is the
3×3 product of those three `P`. Path-independence HOLDs at `s` iff all three
paths exist and the three products are equal. Else fail not `UNDEFINED`.
Reverse HOLDs iff path-independence HOLDs at both reverse probes. Face HOLDs
iff both face probes HOLD. Face is displayed, not adopted. Cover and split
do not score handedness. This is not leftover of nm2frm3pth two-axis
three-path: those bits are the same readout on a different seed with four
tick-0 sites, while this member has six tick-0 sites and a third far-face
pair, and origin `F` HOLDs on the two-axis seed while origin `F` fails here.
This is not leftover of nm2cycfrmhol two-axis unit-square holonomy. This is
not leftover of nm2cycfrmholfz far-face unit-square holonomy: holonomy
reverse HOLDs and holonomy face fails on the z-square of this same seed,
while three-path reverse fails and three-path face fails. This is not leftover
of nm2cycfrmz cyclic-frame transport. This is not leftover of nm2cycfrmfz
far-face cyclic-frame transport: transport face HOLDs on these face probes
while three-path face fails, and transport reverse fails at origin because
origin split fails. This is not leftover of nm2oricyclz cyclic Orient. This
is not leftover of scalar neighbor-read of Orient. This is not leftover of a
unique nonnegative permutation sending. This is not leftover of nm2orichz
leftover-axis. This is not leftover of nm2orionez lex-one. This is not leftover
of nm2chiralz lexicographic unsigned `o1,o2` orientation. This is not leftover
of nm2oridetz unique signed outgoing letters. This is not leftover of nm2axz
axis-cover. This is not leftover of nm2ax12z 1-in 2-out split. This is not
leftover of leftover-of-`M` alone. This is not leftover of leftover-of-`O`
alone. This is not leftover-empty fail of leftover axis. This is not leftover
of nmunopp union. This is not leftover of nmt2opp `M` frozen at `t`. This is
not leftover of nmot2opp two-tick composition. This is not leftover of
nmoutopp untimed eventual-`O`. This is not leftover of mixed #7188 fail/fail.
This is not leftover of the 1-axis opposite two-site seed. This is not leftover
of the same-lock two-site seed. The second pair is a new seed, not a formed
child. The third pair is a new seed, not a formed child. Uniqueness is not
required. Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_farface_opposite_three_path_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_farface_opposite_three_path_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named seed probes. Incoming lock letters are unit nearest-neighbor
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
with determinant `Orient(q)Orient(r)`. Path-independence is equality of the
three length-3 products along the cyclic permutations of `{+e_1,+e_2,+e_3}`.
Reverse and face are scored on that equality at the reverse pair and at the
face pair. Transport of nm2cycfrmz is a different readout: it is existential
at a vertex, not three path products. Unit-square holonomy is a different
readout: it is a four-edge product around a square, not three cube-diagonal
paths. Neighbor-read of the scalar Orient sign is a different readout and is
not used as the object. A unique nonnegative permutation sending is a
different readout and is not used as the object. Named signs `{+,−}` of
locks are a coarser readout and are not used as the object. Occupancy of
sites is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of equality of the three length-3 path-ordered products of cyclic-frame transport along the cyclic permutations of +e1,+e2,+e3 of M and O at t+1 on the three-axis far-face opposite seed, F and Orient at the four seed probes, P on the path edges, the three products at each probe, reverse fail and face fail from path-independence; uniqueness of a sending is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_farface_opposite_three_path_cyclic_frame_transport_tplus1_reverse_face
target_blocker_text: "display three-path cyclic-frame transport reverse/face on the three-axis far-face opposite seed, not nm2frm3pth two-axis three-path, not nm2cycfrmhol two-axis holonomy, not nm2cycfrmholfz far-face holonomy, not nm2cycfrmz transport, not nm2cycfrmfz far-face transport, not scalar neighbor-read of Orient, not unique nonnegative sending, not leftover-axis, not lex-one e1<e2<e3, not unique |O_i|=1, not unsigned axis units, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep three-path cyclic-frame transport of F at t+1 displayed; do not write path-independence into Admissibility, do not reduce to nm2frm3pth two-axis three-path, do not reduce to nm2cycfrmhol two-axis holonomy, do not reduce to nm2cycfrmholfz far-face holonomy, do not reduce to nm2cycfrmz transport, do not reduce to nm2cycfrmfz far-face transport, do not reduce to scalar neighbor-read of Orient, do not reduce to unique nonnegative permutation sending, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-smallest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace path-independence by unique outgoing letters, do not replace path-independence by existential opposite of signed locks, do not replace path-independence by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for equality of the three length-3 path-ordered products of cyclic-frame transport of M and O at t+1 on the three-axis far-face opposite seed and reverse/face from that equality; displayed, not adopted"
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

No larger host is used. The reverse pair and the face pair are the only
starts whose three-path cyclic-frame transport of `F=(m,o_next,o_prev)` of
`M` and `O` is scored:

```text
A = (0,0,0),  B = (0,1,0).
C = (0,0,1),  D = (0,1,1).
```

A start or endpoint outside `B_3(0)` is fail, not `UNDEFINED`. These are not
the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`, `D=(1,0,1)`. These are not
the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`. These are not
the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`. `A` and `B`
are seeds of the first opposite pair. `C` and `D` are seeds of the second
opposite pair. Same process as nm2axz. `F` and Orient as nm2cycfrmhol.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. Site `(0,0,−1)` locks `+e_3`. Site `(0,1,−1)`
locks `−e_3`. The second pair is a new seed, not a formed child of the
first pair. The third pair is a new seed, not a formed child, and sits on
the −z face opposite the z-probes. This seed is not the 1-axis opposite
two-site seed `{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not the
perp two-site seed `+e_1/+e_2`. This seed is not the same-lock two-site
seed `+e_1/+e_1`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site seed
that also records `(0,-1,0)` at tick 0. This seed is not the two-axis
opposite seed of nm2frm3pth.

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

## Named three-path cyclic-frame transport of `(m,o_next,o_prev)` at `τ=t+1`

Let `t(q)` be the formation tick of a probe `q` when that tick is defined in
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

Cyclic frame, edge sending, and three-path independence at the same cut:

```text
When split HOLDs, F(q)=(m, o_next, o_prev).
For an edge q→r of a formed six-neighbor pair, P(q,r) is the
unique 3×3 signed permutation with det = Orient(q)Orient(r)
sending columns of F(q) to columns of F(r) (F(r)=F(q)P).
If none, that edge fails.
For a start s let w=s+e_1+e_2+e_3.
If w·w>9, path-independence at s fails, not UNDEFINED.
The three paths are the walks along
(+e_1,+e_2,+e_3), (+e_2,+e_3,+e_1), (+e_3,+e_1,+e_2).
A path exists iff every vertex is in B_3(0) and formed at τ
and every edge has P.
The path product is the 3×3 product of those three P.
Path-independence HOLDs at s iff all three paths exist and
the three products are equal. Else fail, not UNDEFINED.
If a vertex lies outside B_3(0), the letter fails, not UNDEFINED.
If a path misses, the letter fails, not UNDEFINED.
Uniqueness of a sending neighbor is not required.
```

Neighbor-read of the scalar Orient sign HOLDs at `q` if and only if
`Orient(q)` is `±1` and some formed six-neighbor has the same sign. That
is a different object. Transport of nm2cycfrmz HOLDs at `q` if and only if
some formed six-neighbor hosts a signed-permutation sending. That is a
different object: transport fails at origin and HOLDs at `B,C,D` on this
member, so transport reverse fails and transport face HOLDs, while
three-path reverse fails and three-path face fails. nm2cycfrmfz far-face
cyclic-frame transport reverse HOLDs and face HOLDs on the z-probes of this
same three-axis seed: those bits are existential at those z-probes, not
three cube-diagonal products. nm2cycfrmholfz far-face unit-square holonomy
reverse HOLDs and face fails on `A-D-B-E` and `C-C1-C2-C3` of this same
seed; those squares are not these four seed probes. nm2frm3pth two-axis
three-path is the same product test on four tick-0 sites; here `(0,0,−1)`
is a seed at tick 0 with lock `+e_3`, not a formed child at tick 1, and
origin `F` fails. A unique nonnegative permutation sending is a different
object.

Reverse three-path cyclic-frame transport holds if and only if
path-independence HOLDs at origin and at `(0,1,0)`. Face three-path
cyclic-frame transport holds if and only if path-independence HOLDs at
`(0,0,1)` and at `(0,1,1)`. Either probe `UNDEFINED` is `UNDEFINED`. Else
HOLD or fail as the product test says.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover fails reverse because origin `O` is only
`{−e_2}`, so cover does not occupy `{e_1,e_2,e_3}`, while this reverse
fails from missing paths, not from cover. Identifying split reverse with
this reverse is refused: split fails at origin and HOLDs at `B`.
Identifying leftover-empty fail with this reverse is refused:
leftover-empty fail scores empty leftover as reverse fail, and leftover at
origin is `{e_3}` nonempty while leftover at `B` is empty. Identifying
nm2cycfrmz transport with this reverse is refused: transport reverse fails
from origin split fail, which is existential at a vertex, not three
products. Identifying unit-square holonomy with this reverse is refused:
holonomy reverse HOLDs on this same seed. Identifying nm2frm3pth two-axis
three-path with this reverse is refused: origin `F` HOLDs on the two-axis
seed and fails here.

## Theorem 1 — ticks, `F`, Orient, `P`, the three products at each probe

On this process the four seed probes form in `B_3(0)` at tick 0. Compare to
leftover axis: leftover at origin is `{e_3}` and leftover at `B` is empty.
Compare to nm2axz cover and nm2ax12z split: both fail reverse because origin
cover fails. Compare to nm2oricyclz cyclic Orient: reverse fails from origin
Orient fail. Compare to nm2cycfrmz cyclic-frame transport: reverse fails and
face HOLDs from existential sendings. Compare to scalar neighbor-read of
Orient: fail at origin and HOLD at `B,C,D`, so scalar reverse fails and
scalar face HOLDs. Compare to nm2cycfrmholfz far-face holonomy: reverse HOLDs
and face fails on the unit squares. This display reads the three path-ordered
products of `(m,o_next,o_prev)` from each seed probe:

```text
t(A)=0
t(B)=0
t(C)=0
t(D)=0
M(A, τ) = {+e_1}
M(B, τ) = {−e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_2}
O(A, τ) = {−e_2}
O(B, τ) = {+e_2, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3}
O(D, τ) = {+e_1, −e_1, +e_3}
split(A) = fail
split(B) = hold
split(C) = hold
split(D) = hold
m(A) = +e_1
m(B) = −e_1
i(B) = 1
o_next(B) = +e_2
o_prev(B) = −e_3
det(B) = 1
Orient(A) = fail
Orient(B) = +1
m(C) = +e_2
i(C) = 2
o_next(C) = +e_3
o_prev(C) = −e_1
det(C) = -1
Orient(C) = −1
m(D) = −e_2
i(D) = 2
o_next(D) = +e_3
o_prev(D) = −e_1
det(D) = 1
Orient(D) = +1
F(A) = fail
F(B) = (−e_1, +e_2, −e_3)
F(C) = (+e_2, +e_3, −e_1)
F(D) = (−e_2, +e_3, −e_1)
product(A, e1e2e3) = fail
product(A, e2e3e1) = fail
product(A, e3e1e2) = fail
product(B, e1e2e3) = fail
product(B, e2e3e1) = fail
product(B, e3e1e2) = [0 0 -1; 1 0 0; 0 -1 0]
product(C, e1e2e3) = fail
product(C, e2e3e1) = fail
product(C, e3e1e2) = fail
product(D, e1e2e3) = fail
product(D, e2e3e1) = fail
product(D, e3e1e2) = fail
path-independence(A) = fail
path-independence(B) = fail
path-independence(C) = fail
path-independence(D) = fail
```

Origin is a seed at tick 0 with seed letter `+e_1`. The third far-face pair
occupies `(0,0,−1)` as a seed, so origin outgoing at `τ=1` is only `{−e_2}`:
cover fails, split fails, `F` fails, and every path that starts at origin
misses the first edge. On the two-axis seed of nm2frm3pth, origin outgoing
is `{−e_2,−e_3}`, split HOLDs, and `F=(+e_1,−e_2,−e_3)`. Mixed remains a
set: `O(C,τ)` has three outgoing steps. Unique outgoing letters would assign
`UNDEFINED` at mixed `O`. Unique signed `|O_i|=1` fails at `C` and at `D`
because both have `{±e_1}`. Lex-largest picks `−e` on that mixed cyclic slot.
At `B`, split HOLDs with unique signed `O` on both cyclic axes. Cover and
split do not score handedness. O is not M.

On the 1-axis opposite two-site seed, `C=(0,0,1)` is a formed child at
tick 1 locking `+e_3`. Here both `(0,0,1)` and `(0,1,1)` are seeds of a
second opposite pair on a second axis. Path-independence at the y-probes
and at the x-probes of this same seed is not this letter.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,0)` is a
seed, so it is not a new 6-NN of `A`:

```text
new 6-NN of A at t(A)+1: (0, -1, 0)
new 6-NN of B at t(B)+1: (0, 2, 0)
new 6-NN of C at t(C)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)
new 6-NN of D at t(D)+1: (1, 1, 1), (-1, 1, 1), (0, 1, 2)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at `A,C,D`. At `B`,
`O` at `t` is already `{−e_3}` because the third-pair seed `(0,1,−1)` sits
on that six-neighbor. Path `e3e1e2` from `B` exists: vertices
`(0,1,0)`, `(0,1,1)`, `(1,1,1)`, `(1,2,1)` are formed, every edge has `P`,
and the product is `[0 0 -1; 1 0 0; 0 -1 0]`. Paths `e1e2e3` and `e2e3e1`
from `B` miss, so path-independence at `B` fails. From `C` and from `D`
every cyclic path misses a later vertex whose split fails, so those three
products fail. A start whose endpoint lies outside `B_3(0)`, for example
`(2,2,0)` with `w=(3,3,1)` or `(0,0,4)`, is fail, not `UNDEFINED`.

## Theorem 2 — reverse from three-path cyclic-frame transport at `τ`

Reverse three-path cyclic-frame transport holds if and only if
path-independence HOLDs at origin and at `(0,1,0)`. Origin split fails, so
all three origin products fail. At `(0,1,0)` only path `e3e1e2` exists.
Reverse fails. This is fail iff a path misses or the three products are
unequal, not leftover of nm2cycfrmz cyclic-frame transport, not leftover of
nm2cycfrmholfz far-face unit-square holonomy, not leftover of nm2frm3pth
two-axis three-path, not leftover of nm2oricyclz cyclic Orient equal signs,
not leftover of scalar neighbor-read, not leftover of a unique nonnegative
permutation sending, not leftover of nm2chiralz lexicographic unsigned
`o1,o2`, not leftover of nm2oridetz unique signed outgoing letters, not
leftover of nm2orichz leftover-axis, not leftover of nm2orionez lex-one,
not leftover of nm2axz axis-cover, not leftover of nm2ax12z 1-in 2-out
split, not leftover-empty fail, and not exist-opposite.

Reverse three-path cyclic-frame transport at τ: fail

Both reverse probes are defined, so this is not `UNDEFINED`. Cover reverse
fails because cover fails at origin. Split reverse fails because split fails
at origin. Cover and split do not score handedness. nm2cycfrmz transport
reverse fails because transport fails at origin; that is existential at two
vertices, not the three products. nm2cycfrmholfz holonomy reverse HOLDs on
this same seed; that four-edge identity is not this reverse. On the two-axis
seed, origin `F` HOLDs and three-path reverse still fails from a missed
`e1e2e3` path: leftover of nm2frm3pth, not this origin-`F`-fail. Leftover
of `M` reverse HOLDs because leftover of `M` at `A` is `{e_2,e_3}` and at
`B` is `{e_2,e_3}`: nonempty equal, while this reverse fails. Leftover of `O` at `A` is
`{e_1,e_3}` and at `B` is `{e_1}`: nonempty unequal. Exist-opposite reverse
of signed `M` holds. Exist-opposite reverse of signed `O` holds. Those
leftovers are not this display.

Reverse fails.

## Theorem 3 — face from three-path cyclic-frame transport at `τ`

Face three-path cyclic-frame transport holds if and only if
path-independence HOLDs at `(0,0,1)` and at `(0,1,1)`. Every cyclic path
from each face probe misses a later vertex with split fail, so all six
face products fail. Face fails. Displayed, not adopted.

Face three-path cyclic-frame transport at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face HOLDs because cover HOLDs at `C` and at `D`. Split face HOLDs
because split HOLDs at `C` and at `D`. Those two vertices are the face
probes, and split HOLD there does not make the three paths exist: later
vertices on each walk are 2-in split fail. Cyclic lex-largest oriented face
fails because the signs at `C` and `D` are `−1` and `+1`. nm2cycfrmz
transport face HOLDs because transport HOLDs at `C` and at `D`; that
existential pair is not this three-path letter. Leftover-axis face fails
because those signs are `−1` and `+1`. Leftover of `M` face HOLDs because
leftover of `M` at `C` and at `D` is `{e_1,e_3}` on both sides, while this
face fails. Unique signed face fails because neither unique signed sign is
`±1`. Cover and split do not score handedness. Presence of an opposite pair
in `O` HOLDs at `C` and at `D`, so pair-presence face HOLDs while this face
fails. On the 1-axis opposite two-site seed, `t(C)` is not 0. The four
y-probes of this same seed are not this letter. The four x-probes are not
this letter. A start outside `B_3(0)` is path-independence fail, not
`UNDEFINED`.

Face fails.

## What this note does not claim

- It does not replace three-path independence by nm2cycfrmz cyclic-frame transport.
- It does not replace three-path independence by nm2cycfrmfz far-face cyclic-frame transport.
- It does not reprint nm2frm3pth two-axis three-path as this member.
- It does not reprint nm2cycfrmhol two-axis unit-square holonomy as this member.
- It does not reprint nm2cycfrmholfz far-face unit-square holonomy as this member.
- It does not replace three-path independence by neighbor-read of the scalar Orient sign.
- It does not replace three-path independence by a unique nonnegative permutation sending.
- It does not require a unique formed six-neighbor witness.
- It does not reprint nm2oricyclz cyclic Orient reverse hold face hold as this letter.
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

This display uses Lattice to name `B_3(0)` and the four seed probes. It uses
Qubit only as the algebra of the local possibility domain. It uses Record
only as a boundary: a present lock is content. It does not rewrite
Admissibility. The three-axis far-face opposite seed process, three-path
cyclic-frame transport of `(m,o_next,o_prev)` of `M` and `O` at `t+1`, and
the reverse/face bits from that equality are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three-axis far-face opposite seed `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `0`, `0`, `0` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; origin `{−e_2}`; `B` `{+e_2,−e_3}`; face mixed |
| split at `τ` | Theorem 1; fail at origin; HOLD at `B,C,D` |
| unique signed `m`, axis index `i`, cyclic `(o_next,o_prev)` | Theorem 1; origin plane fail; `B,C,D` defined |
| integer `det(m,o_next,o_prev)` | Theorem 1; origin fail, `B` `+1`, `C` `-1`, `D` `+1` |
| Orient at `τ` | Theorem 1; origin fail, `B` `+1`, `C` `−1`, `D` `+1` |
| cyclic frame `F=(m,o_next,o_prev)` | Theorem 1; origin fail; LIVE at `B,C,D` |
| three path products at each probe | Theorem 1; origin all fail; `B` fail, fail, one matrix; face all fail |
| leftover of nm2cycfrmz cyclic-frame transport | Theorem 1; transport reverse fail and transport face hold; not this letter |
| leftover of nm2cycfrmholfz far-face holonomy | Theorem 1; holonomy reverse hold and holonomy face fail; not this letter |
| leftover of nm2frm3pth two-axis three-path | Theorem 1; origin `F` holds on four tick-0 sites; not this seed |
| reverse from three-path cyclic-frame transport at `τ` | Theorem 2; `fail` |
| face from three-path cyclic-frame transport at `τ` | Theorem 3; `fail` |
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
| leftover of nm2oricyclz cyclic Orient equal signs | not this letter |
| leftover of nm2cycfrmz cyclic-frame transport | not this letter |
| leftover of nm2cycfrmfz far-face cyclic-frame transport | not this letter |
| leftover of nm2cycfrmhol two-axis unit-square holonomy | not this seed; four tick-0 sites |
| leftover of nm2cycfrmholfz far-face unit-square holonomy | not this letter; four-edge square product |
| leftover of nm2frm3pth two-axis three-path | not this seed; four tick-0 sites |
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
| V1 | It answers the first-display question: equality of the three length-3 path-ordered products of cyclic-frame transport of `(m,o_next,o_prev)` of `M` and `O` at `t+1` on the three-axis far-face opposite seed, and reverse/face from that equality. |
| V2 | Current main has no landed three-path cyclic-frame-transport reverse/face of timed `M` and `O` on these four seed probes of the three-axis far-face opposite seed. |
| V3 | Three path products at each of four probes and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the three length-3 signed-permutation products along cyclic permutations of `{+e_1,+e_2,+e_3}` at the same `t+1` cut, reverse fails and face fails while nm2cycfrmz transport reverse fails and transport face HOLDs, nm2cycfrmfz far-face transport reverse HOLDs and face HOLDs on z-probes, nm2cycfrmholfz far-face holonomy reverse HOLDs and face fails on the unit squares, nm2frm3pth two-axis three-path has origin `F` HOLD, scalar neighbor-read reverse fails, and nm2oricyclz Orient equality does not supply the three products. |
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
| scalar neighbor-read of Orient | reuse equal Orient sign at some formed 6-NN | scalar fails at origin and HOLDs at `B,C,D`; scalar reverse fails and scalar face HOLDs while this reverse fails and this face fails | ATTEMPTED |
| unique nonnegative permutation sending | require a unique sending with no minus signs | unique nonnegative sending fails at origin and HOLDs at `B`; uniqueness is not required | ATTEMPTED |
| nm2cycfrmz cyclic-frame transport | reuse transport reverse fail and face hold from existential 6-NN sendings | transport reverse fails and transport face HOLDs while this reverse fails and this face fails; transport is existential at a vertex, three-path is three products | ATTEMPTED |
| nm2oricyclz cyclic Orient | reuse Orient reverse and face from equal `±1` signs | Orient reverse fails from origin fail and Orient face fails from `−1,+1`; HOLDING cyclic #7451/#7452 is the frame sign, not three products | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse and face | unsigned at `B` is `−1` while cyclic Orient at `B` is `+1`; those signs are not the three products | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse and face | unique signed HOLDs at `B` and fails at `C,D`; an opposite pair in face `O` makes `|O_i|≠1` | ATTEMPTED |
| nm2orichz leftover-axis | reuse leftover-axis reverse and face | leftover-axis fails at origin and at `B`; leftover-axis face fails because C and D disagree; those two signs are not three products | ATTEMPTED |
| nm2orionez lex-one | reuse lex-one reverse and face | lex-one at `B` is `−1` from `e1<e2<e3` order independent of `m`; cyclic Orient at `B` is `+1` | ATTEMPTED |
| cyclic lex-smallest | reuse same cyclic axes with `+e` if both signs | lex-smallest face is `+1,−1`; those signs are not these products | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse and cover face on these probes | cover fails reverse and HOLDs face without cyclic signed columns | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse split reverse and split face | split fails reverse and HOLDs face without the three products; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover at origin is `{e_3}` and leftover at `B` is empty, so leftover reverse fails; leftover face fails from empty leftover at both face probes | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` reverse HOLDs (`{e_2,e_3}` at origin and at `B`) while this reverse fails; leftover of `M` face HOLDs while this face fails | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at origin is `{e_1,e_3}` and at `B` is `{e_1}`, nonempty unequal | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `M` and of signed `O` both hold while this reverse fails | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence fails at origin and HOLDs at `C,D`; pair-presence face HOLDs while this face fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-largest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(C,τ)` remains a set | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | at `B`, unsigned incoming Orient is `−1` while cyclic Orient is `+1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; origin is 1-in 1-out cover fail | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED; origin cyclic plane fails from empty `O_next`/`O_prev` | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(C)` as a formed child | different seed; second pair is a new seed, not a formed child; here `t(C)=0` | ATTEMPTED |
| y-probe three-path | score the four y-probes on this seed | y-probe path-independence is not this letter | ATTEMPTED |
| x-probe three-path | score the four x-probes on this seed | x-probe path-independence is not this letter | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores three path products of cyclic-frame transport at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face fail from missed cube-diagonal paths on the three-axis far-face opposite seed | ATTEMPTED |
| nm2cycfrmhol two-axis holonomy | reuse reverse hold and face fail of unit squares on four tick-0 sites | different seed; this member has six tick-0 sites | ATTEMPTED |
| nm2cycfrmholfz far-face holonomy | reuse reverse hold and face fail of `A-D-B-E` and `C-C1-C2-C3` | holonomy reverse HOLDs while this reverse fails; holonomy is a four-edge square, not three cube-diagonal paths | ATTEMPTED |
| nm2cycfrmfz far-face transport | reuse transport reverse hold and face hold on z-probes of this three-axis seed | those z-probes are not origin and `(0,1,0)`; transport face HOLDs on these face probes while this face fails | ATTEMPTED |
| nm2frm3pth two-axis three-path | reuse the same three products on four tick-0 sites | different seed; origin `F` HOLDs there and fails here | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is three disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of path-independence with
leftover of `M` alone, missing identification of path-independence with
leftover-empty fail, missing identification of path-independence with
existential opposite of signed locks, missing identification of
path-independence with presence of an opposite pair in `O`, missing
identification of path-independence with nm2chiralz lexicographic unsigned
`o1,o2`, missing identification of path-independence with nm2oridetz unique
signed `|O_i|=1`, missing identification of path-independence with
nm2orichz leftover-axis, missing identification of path-independence with
nm2orionez lex-one, missing identification of path-independence with cyclic
lex-smallest, missing identification of path-independence with nmcover
axis-cover, missing identification of path-independence with nm2axz
axis-cover, missing identification of path-independence with nm2ax12z 1-in
2-out split, missing identification of this seed with the 1-axis opposite
two-site seed, and missing Record identification of three-path reverse are
distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three disjoint opposite seed pairs `+e_1/−e_1`,
`+e_2/−e_2`, and `+e_3/−e_3`, perpendicular step rule, incoming-step lock,
own incoming set and own outgoing dual from records with tick `<= τ`,
per-probe `τ=t+1`, unsigned axis, cover as complementary occupation of
`{e_1,e_2,e_3}`, split as cover and `|Axis(M)|=1`, unique signed `m` when
split HOLDs, cyclic next/prev axes of `Axis(M)`, lex-largest signed
outgoing letter under `+e < −e` (hence `−e` if both signs), integer
determinant sign, empty `O_next` or empty `O_prev` as Orient fail not
`UNDEFINED`, split fail as Orient fail not `UNDEFINED`, four seed probes
with origin `A`, second pair as a new seed not a formed child, third pair
as a new seed not a formed child on the −z face, three cyclic permutations
of `{+e_1,+e_2,+e_3}`, miss as fail not `UNDEFINED`, endpoint outside
`B_3(0)` as fail not `UNDEFINED`, and mixed remains a set are declared. No
uniqueness of outgoing locks, no six-neighbor lock union as the scored
object, no lock-count clock, no global later T, no formation attachment
from already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
path-independence `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | cyclic frame `F=(m,o_next,o_prev)` and three length-3 path-ordered products | no continuum alphabet |
| per site | reverse origin,`(0,1,0)` and face `(0,0,1)`,`(0,1,1)` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | three path products, reverse/face from path-independence | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for three-path cyclic-frame
transport reverse/face, a formation-rate rule, and a physical selector among
1-in 2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Three-path reverse fail and face fail are only leftover of
nm2frm3pth two-axis three-path, or of nm2cycfrmholfz far-face unit-square
holonomy, or of nm2cycfrmz cyclic-frame transport, or of nm2cycfrmfz
far-face transport, or of nm2oricyclz cyclic Orient, or of neighbor-read of
the scalar Orient sign, or of cover and split; leftover of `M` alone already
answers reverse HOLD; exist-opposite of signed `O` already answers reverse;
mixed #7188 already reported fail/fail; the second pair is only the formed
child `(0,0,1)` of the 1-axis seed; the third pair is only the formed child
`(0,0,−1)` of the two-axis seed; unique outgoing letters should be required;
and unsigned incoming axis already gives the same signs because each `M`
letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Three-path reverse fails because origin split fails, so every
origin path misses, and because at `(0,1,0)` only path `e3e1e2` exists.
Three-path face fails because every cyclic path from `C` and from `D`
misses. Transport reverse fails and transport face HOLDs: leftover of
nm2cycfrmz cyclic-frame transport, not this letter. nm2cycfrmfz far-face
transport reverse HOLDs and face HOLDs on the z-probes of this same
three-axis seed: leftover of existential sendings at those z-probes, not
three cube-diagonal products. nm2cycfrmholfz far-face holonomy reverse HOLDs
and face fails with a four-edge product on the unit squares; holonomy
reverse HOLDs while this reverse fails. nm2frm3pth two-axis three-path is
the same product test on four tick-0 sites; here the third pair is a new
seed, not a formed child, and origin `F` fails. Scalar neighbor-read of
Orient fails at origin and HOLDs at `B,C,D`, so scalar reverse fails and
scalar face HOLDs. Unique nonnegative permutation sending fails at origin
and HOLDs at `B`. Cover reverse fails and split reverse fails; cover face
HOLDs and split face HOLDs. Leftover of `M` reverse HOLDs while this reverse
fails. Exist-opposite reverse of signed `M` and of signed `O` both HOLD
while this reverse fails. Unique outgoing letters would assign `UNDEFINED`
at mixed `O(C)`; this Orient at `C` is `−1`, not `UNDEFINED`. Mixed #7188
is a different z-symmetric process with mixed `M`. The second pair is a new
seed, not a formed child: `(0,0,1)` is recorded at tick 0 with lock `+e_2`,
whereas the 1-axis child forms at tick 1 with lock `+e_3`. The third pair is
a new seed, not a formed child: `(0,0,−1)` is recorded at tick 0 with lock
`+e_3`, whereas the two-axis child forms at tick 1. At `B`, unsigned
incoming Orient is `−1` while cyclic Orient is `+1`.

### N8 — cross-cycle echo

nm2axz cover on this three-axis far-face seed reported cover HOLD at each of
the four z-probes, reverse hold, and face hold. nm2ax12z 1-in 2-out split on
the same seed reported split HOLD at each of the four z-probes, reverse hold,
and face hold. nm2chiralz lexicographic unsigned `o1,o2` on the same seed
reported Orient `−1,+1,+1,+1`, reverse fail, and face hold. nm2oridetz
unique signed outgoing letters on the same seed reported Orient fail at
each z-probe, reverse fail, and face fail. nm2orichz leftover-axis on the
same seed reported Orient `−1,−1,+1,−1`, reverse hold, and face fail
because C and D swap `(m,pair)` columns. nm2orionez lex-one on the same
seed reported Orient `−1,+1,−1,−1`, reverse fail, and face hold from
`e1<e2<e3` order independent of `m`. Leftover axis reported empty leftover
at each of four z-probes, leftover reverse fail, and leftover face fail.
The four y-probes of this same seed reported cyclic Orient `+1` at y-probe
`A` from `m=−e_1` and Orient fail at y-probe `D` from split fail, so
y-reverse fails and y-face fails. nm2oricyclz cyclic next/prev lex-largest
Orient on the same seed reported HOLDING cyclic #7451/#7452 with Orient
`−1,−1,+1,+1`, reverse hold, and face hold from equal signs, without a
sending matrix. nm2cycfrmz and nm2cycfrmfz reported transport reverse HOLD
and transport face HOLD on the z-probes. nm2cycfrmholfz reported holonomy
reverse HOLD and holonomy face fail on the unit squares. This note is not
those displays: it reports equality of the three length-3 path-ordered
products of cyclic-frame transport of `(m,o_next,o_prev)` of `M` and `O` at
`τ=t+1` on the three-axis far-face opposite seed, with `t(A)=0`, `t(B)=0`,
`t(C)=0`, and `t(D)=0`, reverse fail, and face fail, while origin `F` fails
because the third pair is a seed, while nm2frm3pth two-axis three-path has
origin `F` HOLD, while holonomy reverse HOLDs on this same seed, and while
transport face HOLDs on these face probes. Cover and split do not score
handedness. The third pair is a new seed, not a formed child.

**Gate disposition:** PASS for the three-path cyclic-frame-transport `t+1`
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
nm2cycfrmfz far-face cyclic-frame transport HOLD,” “the predicate equals
nm2cycfrmhol two-axis unit-square holonomy HOLD,” “the predicate equals
nm2cycfrmholfz far-face unit-square holonomy HOLD,” “the predicate equals
nm2frm3pth two-axis three-path HOLD,” “the predicate equals scalar
neighbor-read of Orient HOLD,” “the predicate equals unique nonnegative
permutation sending HOLD,” “the predicate equals nmcover axis-cover HOLD,”
“the predicate equals nm2axz axis-cover HOLD,” “the predicate equals
nm2ax12z 1-in 2-out split HOLD,” “the predicate equals the 1-axis opposite
two-site seed,” “the predicate equals nmunopp union,” “bits are
Admissibility,” “split fail is UNDEFINED,” or “empty `O_i` is UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis far-face
opposite perp-step incoming-lock process, reads each seed probe's own earliest
incoming set and own outgoing dual from the record prefix at that vertex's
`t+1`, reports split of the pair, reports the cyclic frame
`F=(m,o_next,o_prev)` as nm2cycfrmz, reports Orient as nm2oricyclz
lex-largest cyclic, reports `P` on each formed six-neighbor edge of the
three cyclic paths from each probe, reports the three path products, lists
new records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that reverse
path-independence fails and face path-independence fails, that a start or
endpoint outside `B_3(0)` is fail not `UNDEFINED`, that nm2cycfrmz transport
reverse fails and transport face HOLDs while three-path face fails, that
nm2cycfrmholfz holonomy reverse HOLDs while three-path reverse fails, that
nm2frm3pth two-axis three-path is a different member with origin `F` HOLD,
that scalar neighbor-read fails at origin, that unique nonnegative
permutation sending HOLDs at `B` and fails at origin, that leftover of `M`
reverse HOLDs while this reverse fails, that split fail is path-independence
fail not `UNDEFINED`, that empty `O_next` or empty `O_prev` is Orient fail
not `UNDEFINED`, that the 1-axis opposite two-site seed is a different
member, that #7477 same-lock is a different member, that LIVE three-axis as
a three-site seed is a different member, that leftover-empty fail is a
different predicate, that leftover of `M` alone and leftover of `O` alone
are different objects, that mixed sets remain sets, that the construction
does not sum, that a formation member from already-recorded six-neighbor
locks is not attached, that the second pair is a new seed not a formed
child, that the third pair is a new seed not a formed child, that the
y-probes and x-probes of this seed are not this letter, and that the
display is not the two-tick lock-count clock composition. No runner cache
is written.
