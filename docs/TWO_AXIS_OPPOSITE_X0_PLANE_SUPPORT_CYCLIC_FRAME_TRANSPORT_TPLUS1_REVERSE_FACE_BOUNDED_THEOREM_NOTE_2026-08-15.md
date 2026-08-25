---
claim_id: two_axis_opposite_x0_plane_support_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Plane support of cyclic-frame transport on the x=0 versus x=1 formed sites in B_3 at t+1 on the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_x0_plane_support_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# X=0 Plane Support Of Cyclic-Frame Transport At t+1 Reverse And Face Versus The X=1 Plane On The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** plane support of cyclic-frame transport of `(m,o_next,o_prev)` of
simultaneous earliest incoming set `M` and outgoing dual `O` at each formed
site's `τ=t+1`, on the formed-at-τ sites of the `x=0` plane versus the `x=1`
plane in `B_3(0)={n:n·n<=9}` of the two-axis opposite seed. Same process as
nm2axz. Transport as nm2cycfrmz. `M`, `O`, split as nm2ax12z. Orient as
nm2oricyclz (lex-largest cyclic); HOLDING cyclic #7451/#7452. Let `t(q)`
be the formation tick of site `q`. Let `τ(q)=t(q)+1`. There is no global T.
`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. Seeds are a singleton seed letter.
`O(q,τ)` is the outgoing dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}`
such that `q+e` is formed and `e` is in `M(q+e,τ)`. Unformed at `τ` is
`UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Axis of a defined lock
set `S` is `Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only
if `Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)`
equals `{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
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
transport fails, not `UNDEFINED`. Let Q0 = formed-at-τ sites q in B_3(0)
with q_1=0. Let Q1 = formed-at-τ sites q in B_3(0) with q_1=1. A formed
site is formed at its own `τ=t+1`. Empty Q0 or Q1 is fail, not UNDEFINED.
Reverse HOLDs if and only if `Q0` is nonempty and transport HOLDs at every
`q` in `Q0`. Face HOLDs if and only if `Q1` is nonempty and transport
HOLDs at every `q` in `Q1`. Not a 6-NN forall. HOLDING transport #7490 on
the four z-probes, HOLDING existential neighbor-read #7511, and universal
6-NN neighbor-read fail/fail #7556 are leftover. Cover and split do not
score handedness. This is not leftover of nm2cycfrmz cyclic-frame
transport reverse HOLD whose sending inspects a signed permutation on
four z-probes. This is not leftover of existential neighbor-read of
transport. This is not leftover of universal 6-NN neighbor-read. This is
not leftover of early-tick plane support whose `ticks<=1` restriction
HOLDs on both planes. This is not leftover of equal transport bits
including fail=fail. This is not leftover of nm2oricyclz cyclic Orient
reverse HOLD whose bits are equal `±1` signs, not a signed-permutation
sending. This is not leftover of scalar neighbor-read of Orient. This is
not leftover of a unique nonnegative permutation sending. This is not
leftover of nm2orichz leftover-axis reverse HOLD whose face fails because
C and D swap `(m,pair)` columns. This is not leftover of nm2orionez
lex-one reverse fail whose face HOLDs from `e1<e2<e3` order independent
of `m`. This is not leftover of nm2chiralz lexicographic unsigned `o1,o2`
orientation. This is not leftover of nm2oridetz unique signed outgoing
letters. This is not leftover of nm2axz axis-cover. This is not leftover
of nm2ax12z 1-in 2-out split. This is not leftover of leftover-of-`M`
alone. This is not leftover of leftover-of-`O` alone. This is not
leftover-empty fail of leftover axis. This is not leftover of nmunopp
union. This is not leftover of nmt2opp `M` frozen at `t`. This is not
leftover of nmot2opp two-tick composition. This is not leftover of
nmoutopp untimed eventual-`O`. This is not leftover of mixed #7188
fail/fail. This is not leftover of the 1-axis opposite two-site seed.
This is not leftover of the same-lock two-site seed. The second pair is a
new seed, not a formed child. Uniqueness is not required. Mixed remains a
set. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_x0_plane_support_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_x0_plane_support_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the formed sites of the `x=0` and `x=1` planes. Incoming lock letters are
unit nearest-neighbor steps. `O` is the outgoing dual of those incoming sets
at the per-site cut `τ=t+1`. Axis is the unsigned lattice direction of a
signed lock. Cover is the complementary occupation of `{e_1,e_2,e_3}` by
`Axis(M)` and `Axis(O)`. Split is cover together with `|Axis(M)|=1`. The
cyclic next/prev lex-largest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m` and the
lex-largest signed outgoing letter on the cyclic next and prev axes of
`Axis(M)` under `+e < −e`. When split HOLDs, `F=(m,o_next,o_prev)` is
that LIVE three-axis frame. Transport is existential: some formed
six-neighbor hosts a split-HOLDING frame whose columns are a signed
permutation of the source columns with determinant the product of the
two Orient signs. `Q0` and `Q1` are the formed-at-τ sites of those two
planes. Reverse and face are scored on forall transport HOLD on `Q0` and
on `Q1`. Occupancy of sites is not used. A six-neighbor star is not the
letter. O is not M.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of plane support of cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 on the formed-at-tau x=0 versus x=1 sites of the two-axis opposite seed, Q0, Q1, t and transport bit at each listed site, reverse fail and face fail from those plane foralls; uniqueness of a failing site is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_x0_plane_support_cyclic_frame_transport_tplus1_reverse_face
target_blocker_text: "display forall formed sites on the x=0 plane in B_3, transport HOLDs, versus the x=1 plane, not leftover of HOLDING z-probe transport #7490, not leftover of existential neighbor-read #7511, not leftover of universal 6-NN neighbor-read fail/fail #7556, not a 6-NN forall, not early-tick restriction, not scalar neighbor-read of Orient, not unique nonnegative sending, not leftover-axis, not lex-one e1<e2<e3, not unique |O_i|=1, not unsigned axis units, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep plane support of cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 displayed; do not write plane support into Admissibility, do not reduce to 6-NN forall, do not reduce to nm2cycfrmz four-probe sending, do not reduce to existential neighbor-read, do not reduce to universal 6-NN neighbor-read, do not reduce to early-tick plane support, do not reduce to equal transport bit including fail, do not reduce to scalar neighbor-read of Orient, do not reduce to unique nonnegative permutation sending, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-smallest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace plane support by unique outgoing letters, do not replace plane support by existential opposite of signed locks, do not replace plane support by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for plane support of cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 on the x=0 versus x=1 formed sites of the two-axis opposite seed and reverse/face from that plane support; displayed, not adopted"
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

No larger host is used. The scored sites are every formed site of the `x=0`
plane and every formed site of the `x=1` plane. The four z-probes
`A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`, `D=(1,0,1)` sit inside those planes
and are leftover of HOLDING transport #7490, not the object. These are not
the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`. These are
not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`. Same
process as nm2axz.

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

## Named plane support of cyclic-frame transport of `(m,o_next,o_prev)` at `τ=t+1`

Let `t(q)` be the formation tick of site `q` when that tick is defined in
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

Cover at a site at the same cut:

```text
cover(q) HOLDs iff Axis(M) intersect Axis(O) is empty
and Axis(M) union Axis(O) equals {e_1,e_2,e_3}.
```

Split at a site at the same cut:

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

Q0 = formed-at-τ sites q in B_3(0) with q_1=0.
Q1 = formed-at-τ sites q in B_3(0) with q_1=1.
A formed site is formed at its own τ=t(q)+1.
Empty Q0 or Q1 is fail, not UNDEFINED.
Reverse HOLDs iff Q0 is nonempty and transport HOLDs at every q in Q0.
Face HOLDs iff Q1 is nonempty and transport HOLDs at every q in Q1.
Not a 6-NN forall.
Uniqueness of a failing q is not required.
```

HOLDING transport #7490 on the four z-probes HOLDs at `A,B,C,D` and is a
different object: those four sites are a subset of `Q0 ∪ Q1`. Existential
neighbor-read of HOLDING #7511 HOLDs if some formed six-neighbor has
transport HOLD; that leftover HOLDs at each of the four z-probes. Universal
6-NN neighbor-read fail/fail #7556 HOLDs at `q` iff transport HOLDs at `q`
and every formed 6-NN in `N(q)` has transport HOLD; that leftover fails
reverse and face on the four z-probes. Early-tick plane support restricts
to `ticks<=1` and HOLDs on both planes; that leftover is not this letter.

Reverse x=0 plane support of cyclic-frame transport holds if and only if
`Q0` is nonempty and transport HOLDs at every site in `Q0`. Face x=1 plane
support of cyclic-frame transport holds if and only if `Q1` is nonempty
and transport HOLDs at every site in `Q1`. Empty Q0 or Q1 is fail, not
UNDEFINED. Else if every listed transport HOLDs, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness.

## Theorem 1 — ticks, `Q0`, `Q1`, and transport bit at each listed site at `τ=t+1`

On this process the `x=0` and `x=1` planes form inside `B_3(0)`. Compare to
HOLDING transport #7490: the four z-probes all HOLD. Compare to existential
neighbor-read #7511: some 6-NN HOLDs at each of those probes. Compare to
universal 6-NN neighbor-read #7556: reverse fail and face fail from `N(q)`,
not from a plane. This display reads the forall on formed-at-τ plane sites:

```text
|Q0|=27
|Q1|=25
hold-count(Q0) = 10
fail-count(Q0) = 17
hold-count(Q1) = 10
fail-count(Q1) = 15
t((0, -3, 0))=5
transport((0, -3, 0)) = fail
t((0, -2, -2))=4
transport((0, -2, -2)) = fail
t((0, -2, -1))=3
transport((0, -2, -1)) = fail
t((0, -2, 0))=4
transport((0, -2, 0)) = fail
t((0, -2, 1))=3
transport((0, -2, 1)) = fail
t((0, -2, 2))=4
transport((0, -2, 2)) = fail
t((0, -1, -2))=3
transport((0, -1, -2)) = fail
t((0, -1, -1))=2
transport((0, -1, -1)) = fail
t((0, -1, 0))=1
transport((0, -1, 0)) = hold
t((0, -1, 1))=2
transport((0, -1, 1)) = fail
t((0, -1, 2))=2
transport((0, -1, 2)) = fail
t((0, 0, -3))=5
transport((0, 0, -3)) = fail
t((0, 0, -2))=4
transport((0, 0, -2)) = fail
t((0, 0, -1))=1
transport((0, 0, -1)) = hold
t((0, 0, 0))=0
transport((0, 0, 0)) = hold
t((0, 0, 1))=0
transport((0, 0, 1)) = hold
t((0, 0, 2))=1
transport((0, 0, 2)) = hold
t((0, 1, -2))=4
transport((0, 1, -2)) = fail
t((0, 1, -1))=1
transport((0, 1, -1)) = hold
t((0, 1, 0))=0
transport((0, 1, 0)) = hold
t((0, 1, 1))=0
transport((0, 1, 1)) = hold
t((0, 1, 2))=1
transport((0, 1, 2)) = hold
t((0, 2, -2))=3
transport((0, 2, -2)) = fail
t((0, 2, -1))=2
transport((0, 2, -1)) = fail
t((0, 2, 0))=1
transport((0, 2, 0)) = hold
t((0, 2, 1))=2
transport((0, 2, 1)) = fail
t((0, 2, 2))=2
transport((0, 2, 2)) = fail
t((1, -2, -2))=5
transport((1, -2, -2)) = fail
t((1, -2, -1))=4
transport((1, -2, -1)) = fail
t((1, -2, 0))=3
transport((1, -2, 0)) = hold
t((1, -2, 1))=4
transport((1, -2, 1)) = fail
t((1, -2, 2))=4
transport((1, -2, 2)) = fail
t((1, -1, -2))=4
transport((1, -1, -2)) = fail
t((1, -1, -1))=3
transport((1, -1, -1)) = fail
t((1, -1, 0))=2
transport((1, -1, 0)) = hold
t((1, -1, 1))=2
transport((1, -1, 1)) = hold
t((1, -1, 2))=3
transport((1, -1, 2)) = fail
t((1, 0, -2))=3
transport((1, 0, -2)) = hold
t((1, 0, -1))=2
transport((1, 0, -1)) = hold
t((1, 0, 0))=2
transport((1, 0, 0)) = fail
t((1, 0, 1))=1
transport((1, 0, 1)) = hold
t((1, 0, 2))=2
transport((1, 0, 2)) = fail
t((1, 1, -2))=3
transport((1, 1, -2)) = hold
t((1, 1, -1))=2
transport((1, 1, -1)) = hold
t((1, 1, 0))=2
transport((1, 1, 0)) = fail
t((1, 1, 1))=1
transport((1, 1, 1)) = hold
t((1, 1, 2))=2
transport((1, 1, 2)) = fail
t((1, 2, -2))=4
transport((1, 2, -2)) = fail
t((1, 2, -1))=3
transport((1, 2, -1)) = fail
t((1, 2, 0))=2
transport((1, 2, 0)) = fail
t((1, 2, 1))=2
transport((1, 2, 1)) = hold
t((1, 2, 2))=3
transport((1, 2, 2)) = fail
fail-witness(Q0) = (0, -3, 0)
fail-witness(Q1) = (1, -2, -2)
```

`A=(0,0,1)` and `C=(0,0,2)` lie in `Q0` with transport HOLD. `B=(1,1,1)`
and `D=(1,0,1)` lie in `Q1` with transport HOLD. Those four HOLDING
z-probes are leftover of #7490. First fail-witness in lex order on `Q0`
is `(0,-3,0)` at tick 5. First fail-witness in lex order on `Q1` is
`(1,-2,-2)` at tick 5. Uniqueness of a failing site is not required.
Restricting to `ticks<=1` leaves ten `Q0` sites and two `Q1` sites, all
with transport HOLD; that early-tick plane support is leftover, not this
letter. The `x=3` slice of `B_3(0)` is empty of formed sites, so that
empty plane is fail, not `UNDEFINED`. The `y=0` formed plane is a
different slice and is not this letter. Mixed remains a set. O is not M.

## Theorem 2 — reverse from x=0 plane support of cyclic-frame transport at `τ`

Reverse x=0 plane support of cyclic-frame transport holds if and only if
`Q0` is nonempty and transport HOLDs at every `q` in `Q0`. `Q0` has 27
formed sites and 17 of them fail transport. Reverse fails. This is HOLD
iff every formed-at-τ site on `x=0` transports, not leftover of HOLDING
transport #7490 whose reverse HOLDs on `A` and `B`, not leftover of
existential neighbor-read of HOLDING #7511 whose reverse HOLDs, not
leftover of universal 6-NN neighbor-read fail/fail #7556 whose reverse
fails from `N(B)` rather than from `(0,-3,0)`, not leftover of early-tick
plane support whose reverse HOLDs, not leftover of equal transport bits
including fail=fail, not leftover of nm2oricyclz cyclic Orient equal
signs, not leftover of scalar neighbor-read, not leftover of a unique
nonnegative permutation sending, not leftover of nm2chiralz lexicographic
unsigned `o1,o2`, not leftover of nm2oridetz unique signed outgoing
letters, not leftover of nm2orichz leftover-axis, not leftover of
nm2orionez lex-one, not leftover of nm2axz axis-cover, not leftover of
nm2ax12z 1-in 2-out split, not leftover-empty fail, and not
exist-opposite.

Reverse x=0 plane support of cyclic-frame transport at τ: fail

Both sides are defined and `Q0` is nonempty, so this is not `UNDEFINED`.
Cover reverse HOLDs because cover HOLDs at `A` and at `B`. Split reverse
HOLDs because split HOLDs at `A` and at `B`. Cover and split do not score
handedness. Transport reverse HOLDs because transport HOLDs at `A` and at
`B`. Existential neighbor-read reverse HOLDs because existential
neighbor-read HOLDs at `A` and at `B`. Universal 6-NN neighbor-read
reverse fails because universal neighbor-read fails at `B`. This reverse
fails because `(0,-3,0)` is a formed-at-τ site of the `x=0` plane whose
transport fails. That failing site is not a 6-NN of `A`.

Reverse fails.

## Theorem 3 — face from x=1 plane support of cyclic-frame transport at `τ`

Face x=1 plane support of cyclic-frame transport holds if and only if
`Q1` is nonempty and transport HOLDs at every `q` in `Q1`. `Q1` has 25
formed sites and 15 of them fail transport. Face fails.

Face x=1 plane support of cyclic-frame transport at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face HOLDs because cover HOLDs at `C` and at `D`. Split face HOLDs
because split HOLDs at `C` and at `D`. Existential neighbor-read face
HOLDs because existential neighbor-read HOLDs at `C` and at `D`. Transport
face HOLDs because transport HOLDs at `C` and at `D`. Universal 6-NN
neighbor-read face fails because universal neighbor-read fails at `C` and
at `D`. This face fails because `(1,-2,-2)` is a formed-at-τ site of the
`x=1` plane whose transport fails. Early-tick face HOLDs because the two
`ticks<=1` sites of `Q1` are `D=(1,0,1)` and `B=(1,1,1)`, both with
transport HOLD. Empty leftover does not make reverse `UNDEFINED`.
Leftover-empty fail is not this reverse. On the 1-axis opposite two-site
seed, both plane foralls fail. On the same-lock two-site seed, both plane
foralls fail. On the LIVE three-axis three-site seed, both plane foralls
fail. Those seeds are different members.

Face fails.

## What this note does not claim

- It does not replace plane support of transport by HOLDING z-probe transport #7490.
- It does not replace plane support of transport by existential neighbor-read of HOLDING #7511.
- It does not replace plane support of transport by universal 6-NN neighbor-read fail/fail #7556.
- It does not replace plane support by early-tick plane support on `ticks<=1`.
- It does not replace plane support of transport by nm2cycfrmz signed-permutation sending on four z-probes.
- It does not replace plane support by equal transport bits including fail=fail.
- It does not replace plane support of transport by neighbor-read of the scalar Orient sign.
- It does not replace plane support of transport by a unique nonnegative permutation sending.
- It does not require a unique formed six-neighbor witness.
- It does not reprint nm2oricyclz cyclic Orient reverse hold face hold as this plane support.
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

This display uses Lattice to name `B_3(0)` and the `x=0` and `x=1` planes. It
uses Qubit only as the algebra of the local possibility domain. It uses Record
only as a boundary: a present lock is content. It does not rewrite
Admissibility. The two-axis opposite seed process, plane support of
cyclic-frame transport of `(m,o_next,o_prev)` of `M` and `O` at `t+1`, and
the reverse/face bits from that plane support are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks of every formed-at-τ site in `Q0` and `Q1` | Theorem 1 |
| transport bit of every formed-at-τ site in `Q0` and `Q1` | Theorem 1; 10 HOLD and 17 fail on `Q0`; 10 HOLD and 15 fail on `Q1` |
| reverse from x=0 plane support of cyclic-frame transport at `τ` | Theorem 2; `fail` |
| face from x=1 plane support of cyclic-frame transport at `τ` | Theorem 3; `fail` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of HOLDING z-probe transport #7490 | not this plane forall |
| leftover of existential neighbor-read of HOLDING #7511 | not this plane forall |
| leftover of universal 6-NN neighbor-read fail/fail #7556 | not this plane forall |
| leftover of early-tick plane support | not this plane forall |
| leftover of nm2cycfrmz cyclic-frame transport sending | not this plane forall |
| leftover of equal transport bits including fail=fail | not this plane forall |
| leftover of scalar neighbor-read of Orient | not this plane forall |
| leftover of unique nonnegative permutation sending | not this plane forall |
| leftover of leftover-empty fail of leftover axis | not this oriented display |
| leftover of exist-opposite HOLD | not this oriented display |
| leftover of nmcover axis-cover HOLD | not this oriented display |
| leftover of nm2axz axis-cover HOLD | not this oriented display |
| leftover of nm2ax12z 1-in 2-out split HOLD | not this oriented display |
| leftover of nm2chiralz lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichz leftover-axis | not this oriented display |
| leftover of nm2orionez lex-one signed `e1<e2<e3` | not this oriented display |
| leftover of cyclic lex-smallest | not this oriented display |
| leftover of nm2oricyclz cyclic Orient equal signs | not this plane forall |
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
| empty `Q0` or empty `Q1` scored as `UNDEFINED` | refused; plane-support fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: forall formed sites on the x=0 plane in `B_3`, transport HOLDs, versus the x=1 plane, and reverse/face from that plane support. |
| V2 | Current main has no landed x=0 versus x=1 plane support of cyclic-frame-transport reverse/face of timed `M` and `O` on the two-axis opposite seed. |
| V3 | Plane-support reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the transport HOLD bit at every formed-at-τ site of two named planes at the same `t+1` cut, reverse fails and face fails while four-probe transport reverse HOLDs and four-probe transport face HOLDs, existential neighbor-read reverse HOLDs and existential face HOLDs, universal 6-NN reverse fails from `N(q)` rather than from `(0,-3,0)`, and early-tick plane support HOLDs on both planes. |
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
| HOLDING z-probe transport #7490 | reuse transport HOLD at `A,B,C,D` | four-probe reverse HOLDs and four-probe face HOLDs; this reverse fails and this face fails from plane sites off those probes | ATTEMPTED |
| existential neighbor-read of HOLDING #7511 | reuse some formed 6-NN with transport HOLD | existential HOLDs at `A,B,C,D` and reverse HOLDs and face HOLDs; this reverse fails and this face fails | ATTEMPTED |
| universal 6-NN neighbor-read fail/fail #7556 | reuse every formed 6-NN in `N(q)` | universal reverse fails from `N(B)` containing `(1,1,2)`; this reverse fails from `(0,-3,0)`, which is not a 6-NN of `A`. Not a 6-NN forall | ATTEMPTED |
| early-tick plane support | restrict `Q0` and `Q1` to `ticks<=1` | that restriction HOLDs reverse and face; this letter uses every formed-at-τ site | ATTEMPTED |
| nm2cycfrmz cyclic-frame transport sending | reuse signed-permutation sending of `F(q)` to `F(r)` | sending inspects `P` at four z-probes; this plane forall requires every formed site of the plane to transport | ATTEMPTED |
| equal transport bits including fail=fail | HOLD if some formed 6-NN has the same transport bit | at `(0,-1,1)` transport fails and a formed 6-NN also fails, so equal-bit HOLDs while plane support fails, not UNDEFINED | ATTEMPTED |
| scalar neighbor-read of Orient | reuse equal Orient sign at some formed 6-NN | scalar HOLDs at `A` and fails at `B,C,D`; this reverse fails from a plane site, not from Orient sign | ATTEMPTED |
| unique nonnegative permutation sending | require a unique sending with no minus signs | unique nonnegative sending fails at each of `A,B,C,D`; uniqueness is not required | ATTEMPTED |
| nm2oricyclz cyclic Orient | reuse Orient reverse hold and face hold from equal `±1` signs | Orient reverse HOLDs and face HOLDs without a signed-permutation sending | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face hold | unsigned reverse fails as this reverse fails; unsigned face HOLDs while this face fails | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed reverse fails and face fails as these bits fail; an opposite pair in `O` makes `|O_i|≠1` | ATTEMPTED |
| nm2orichz leftover-axis | reuse leftover-axis reverse hold and face fail | leftover-axis reverse HOLDs (`−1,−1`) while this reverse fails | ATTEMPTED |
| nm2orionez lex-one | reuse lex-one reverse fail and face hold | lex-one reverse fails from `e1<e2<e3` order independent of `m` as this reverse fails; lex-one face HOLDs while this face fails | ATTEMPTED |
| cyclic lex-smallest | reuse same cyclic axes with `+e` if both signs | lex-smallest reverse HOLDs with `+1,+1` and face HOLDs with `−1,−1` | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse hold and cover face hold on these z-probes | cover HOLDs reverse and face without cyclic signed columns; this reverse fails and this face fails from plane sites | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse split reverse hold and split face hold | split HOLDs reverse and face without cyclic order of `Axis(M)`; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails and leftover face fails as these bits fail, but leftover is unsigned unoccupied axes of `M` and `O`, not plane transport | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` is not plane transport | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` is not plane transport | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `O` holds while this reverse fails | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence HOLDs at each of `A,B,C,D` without cyclic columns | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-largest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O` remains a set | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| empty plane as `UNDEFINED` | treat empty `Q0` or empty `Q1` as unformed | Empty Q0 or Q1 is fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, Orient fail at `C` | different seed; second pair is a new seed, not a formed child | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | this letter is the `x=0` versus `x=1` formed planes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | this letter is the `x=0` versus `x=1` formed planes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores plane forall of transport at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports plane-support reverse fail and face fail on the two-axis opposite seed | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is two disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t` before reading | `τ(q)=t(q)+1` is per-site; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the sites by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
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
missing Record identification of plane support reverse are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-site `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
next/prev axes of `Axis(M)`, lex-largest signed outgoing letter under
`+e < −e` (hence `−e` if both signs), integer determinant sign, empty
`O_next` or empty `O_prev` as Orient fail not `UNDEFINED`, split fail as
Orient fail not `UNDEFINED`, formed-at-τ sites of the `x=0` and `x=1`
planes, empty plane as fail not `UNDEFINED`, second pair as a new seed not
a formed child, and mixed remains a set are declared. No uniqueness of
outgoing locks, no six-neighbor lock union as the scored object, no
lock-count clock, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
plane-support `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | cyclic-frame transport at every formed-at-τ site on the x=0 and x=1 planes | no continuum alphabet |
| per site | formed sites with `q_1=0` and `q_1=1` on `B_3(0)` | no other cubic slices as the letter |
| per mode | no mode calculation | no spectral exhaustion |
| per block | Q0/Q1 transport reports, reverse/face from those plane foralls | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for plane support of
cyclic-frame transport reverse/face, a formation-rate rule, and a
physical selector among 1-in 2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Plane-support reverse fail and face fail are only leftover of
universal 6-NN neighbor-read fail/fail #7556, or of HOLDING z-probe
transport #7490, or of existential neighbor-read of HOLDING #7511, or of
leftover-empty fail, or of nm2cycfrmz cyclic-frame transport sending, or
of equal transport bits including fail=fail, or of nm2oricyclz cyclic
Orient equal signs, or of neighbor-read of the scalar Orient sign, or of
cover and split; leftover-axis already answers reverse HOLD; lex-one
already answers face HOLD; unique signed `|O_i|=1` already answers mixed
`O`; leftover of `M` alone already answers reverse; leftover of `O` alone
already answers reverse; exist-opposite of signed `O` already answers
reverse; mixed #7188 already reported fail/fail; the second pair is only
the formed child `(0,0,1)` of the 1-axis seed; unique outgoing letters
should be required; cyclic lex-smallest already gives the same HOLD bits
with opposite signs; early-tick restriction already HOLDs on both planes;
and unsigned incoming axis already gives the same signs because each `M`
letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Plane-support reverse fails because 17 of 27 formed-at-τ
sites on `x=0` fail transport, with first fail-witness `(0,-3,0)`.
Plane-support face fails because 15 of 25 formed-at-τ sites on `x=1` fail
transport, with first fail-witness `(1,-2,-2)`. HOLDING transport #7490
HOLDs at each of the four z-probes, so four-probe reverse HOLDs and
four-probe face HOLDs; those four sites are a subset, not the plane.
Existential neighbor-read of HOLDING #7511 HOLDs at each of the four
z-probes, so existential reverse HOLDs and existential face HOLDs; that
leftover reads some formed six-neighbor, not every formed site of a plane.
Universal 6-NN neighbor-read fail/fail #7556 reverse fails from `N(B)`
containing `(1,1,2)`; this reverse fails from `(0,-3,0)`, which is not a
6-NN of `A`. Not a 6-NN forall. Early-tick plane support HOLDs reverse
and face. Transport reverse HOLDs and transport face HOLDs from sending
of `F` at `A,B` and at `C,D`. Scalar neighbor-read of Orient HOLDs only
at `A` and fails at `B`, `C`, and `D`. HOLDING cyclic #7451/#7452 Orient
reverse HOLDs from equal signs without a sending matrix. Unique
nonnegative permutation sending fails at each probe. Cover and split HOLD
reverse and face on this member and do not score cyclic signed columns.
Leftover-axis reverse HOLDs with `−1,−1` and face fails with `+1,−1`
because C and D swap `(m,pair)` columns. Lex-one reverse fails from
`e1<e2<e3` order independent of `m`. Lexicographic unsigned `o1,o2`
reverse fails with `−1,+1` and face HOLDs with `+1,+1`. Unique signed
`|O_i|=1` reverse fails and face fails because each z-probe has an
opposite pair in `O`. Cyclic lex-smallest reverse HOLDs with `+1,+1` and
face HOLDs with `−1,−1`. Presence of an opposite pair in `O` HOLDs at each
of the four z-probes without cyclic columns. Unique outgoing letters
would assign `UNDEFINED` at mixed `O`; this Orient is a sign, not
`UNDEFINED`. Mixed #7188 is a different z-symmetric process with mixed
`M`. The second pair is a new seed, not a formed child: `(0,0,1)` is
recorded at tick 0 with lock `+e_2`, whereas the 1-axis child forms at
tick 1 with lock `+e_3`. Plane-support reverse is HOLD iff every
formed-at-τ site on `x=0` transports, not leftover of existential
neighbor-read and not leftover of leftover-axis and not leftover of
nm2orionez lex-one.

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
The four y-probes of this same seed reported cyclic Orient `+1` at `A`
from `m=−e_1` and Orient fail at `D` from split fail, so y-reverse fails
and y-face fails. nm2oricyclz cyclic next/prev lex-largest Orient on the
same seed reported HOLDING cyclic #7451/#7452 with Orient `−1,−1,+1,+1`,
reverse hold, and face hold from equal signs, without a sending matrix.
nm2cycfrmz cyclic-frame transport on the same seed reported HOLDING
transport #7490 at `A,B,C,D`, reverse hold, and face hold. Existential
neighbor-read of that field reported HOLDING #7511 at each of those four
probes. Universal 6-NN neighbor-read of that field reported fail/fail
#7556. This note is not those displays: it reports plane support of
cyclic-frame transport of `(m,o_next,o_prev)` of `M` and `O` at `τ=t+1`
on the two-axis opposite seed, with `|Q0|=27`, `|Q1|=25`,
`transport((0, -3, 0)) = fail`, `transport((1, -2, -2)) = fail`, reverse
fail, and face fail, while four-probe transport HOLDs at `A,B,C,D`. Cover
and split do not score handedness.

**Gate disposition:** PASS for the plane-support of cyclic-frame-transport
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
“the predicate equals nm2oricyclz cyclic Orient HOLD,” “the predicate
equals nm2cycfrmz cyclic-frame transport sending HOLD,” “the predicate
equals existential neighbor-read HOLD,” “the predicate equals universal
6-NN neighbor-read HOLD,” “the predicate equals early-tick plane support
HOLD,” “the predicate equals equal transport bits including fail=fail
HOLD,” “the predicate equals scalar neighbor-read of Orient HOLD,” “the
predicate equals unique nonnegative permutation sending HOLD,” “the
predicate equals nmcover axis-cover HOLD,” “the predicate equals nm2axz
axis-cover HOLD,” “the predicate equals nm2ax12z 1-in 2-out split HOLD,”
“the predicate equals the 1-axis opposite two-site seed,” “the predicate
equals nmunopp union,” “bits are Admissibility,” “split fail is
UNDEFINED,” “empty `O_i` is UNDEFINED,” or “empty `Q0` or empty `Q1` is
UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each formed site's own earliest
incoming set and own outgoing dual from the record prefix at that site's
`t+1`, reports transport as nm2cycfrmz by a signed-permutation sending to
some formed six-neighbor, lists every formed-at-τ site of the `x=0` plane
and of the `x=1` plane with its formation tick and transport bit, and
checks Theorems 1--3. It also checks that reverse fails and face fails
from those plane foralls while four-probe transport reverse HOLDs and
four-probe transport face HOLDs, that existential neighbor-read reverse
HOLDs and existential face HOLDs, that universal 6-NN reverse fails and
universal 6-NN face fails from `N(q)` rather than from the plane
fail-witnesses, that early-tick plane support HOLDs on both planes, that
empty `Q0` or empty `Q1` is fail not `UNDEFINED`, that unique nonnegative
permutation sending fails at each probe, that HOLDING cyclic #7451/#7452
Orient reverse HOLDs without being this plane support, that leftover-axis
face fails because C and D swap `(m,pair)` columns and lex-one reverse
fails from `e1<e2<e3` order independent of `m`, that transport fail at a
plane site is plane-support fail not `UNDEFINED`, that equal transport
bits including fail=fail HOLDs at `(0,-1,1)` while plane support fails,
that empty `O_next` or empty `O_prev` is Orient fail not `UNDEFINED`, that
the 1-axis opposite two-site seed is a different member, that #7477
same-lock is a different member, that LIVE three-axis as a three-site seed
is a different member, that leftover-empty fail is a different predicate,
that leftover of `M` alone and leftover of `O` alone are different
objects, that mixed sets remain sets, that the construction does not sum,
that a formation member from already-recorded six-neighbor locks is not
attached, that the second pair is a new seed not a formed child, that the
y-probes and x-probes of this seed are not this letter, and that the
display is not the two-tick lock-count clock composition. No runner cache
is written.
