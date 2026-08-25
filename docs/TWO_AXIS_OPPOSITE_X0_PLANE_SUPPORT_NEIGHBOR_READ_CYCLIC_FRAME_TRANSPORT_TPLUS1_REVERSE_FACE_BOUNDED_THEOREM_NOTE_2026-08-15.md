---
claim_id: two_axis_opposite_x0_plane_support_neighbor_read_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Plane support of neighbor-read of cyclic-frame transport on the x=0 versus x=1 formed sites in B_3 at t+1 on the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_x0_plane_support_neighbor_read_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Plane Support Of Neighbor-Read Of Cyclic-Frame Transport At t+1 Reverse And Face On The x=0 Versus x=1 Formed Sites

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** plane support of neighbor-read of cyclic-frame transport of
`(m,o_next,o_prev)` of simultaneous earliest incoming set `M` and outgoing
dual `O` at each formed site's `τ=t+1`, and reverse/face from that plane
forall, on the formed-at-τ sites with `q_1=0` versus `q_1=1` in
`B_3(0)={n:n·n<=9}` on the two-axis opposite seed. Same process as nm2axz.
Transport as nm2cycfrmz. `M`, `O`, split as nm2ax12z. Orient as nm2oricyclz
(lex-largest cyclic); HOLDING cyclic #7451/#7452. Let `t(q)` be the
formation tick of site `q`. Let `τ(q)=t(q)+1`. There is no global T.
`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. Seeds are a singleton seed letter.
`O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Axis
of a defined lock set `S` is `Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs
at `q` if and only if `Axis(M)` intersect `Axis(O)` is empty and `Axis(M)`
union `Axis(O)` equals `{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if
cover HOLDs and `|Axis(M)|=1` (hence `|Axis(O)|=2`). When split HOLDs, `m`
is unique in `M`. Let `i` in `{1,2,3}` be the axis index of `m`.
`e_next = e_{i+1}` with `3+1→1`. `e_prev = e_{i-1}` with `1−1→3`.
`O_next = O ∩ {±e_next}`. `O_prev = O ∩ {±e_prev}`. If either empty,
Orient fails, not `UNDEFINED`. Order `+e < −e`. `o_next` is the
lex-largest vector in `O_next` (hence `−e` if both signs). `o_prev`
likewise. `Orient(q)` is the sign of the integer determinant of the 3×3
matrix with columns `m`, `o_next`, `o_prev`. If split fails, Orient fails,
not `UNDEFINED`. When split HOLDs, `F(q)=(m,o_next,o_prev)` is an oriented
lattice frame: a LIVE three-axis 1-in 2-out triple. Transport HOLDs at `q`
if and only if split HOLDs at `q`, `Orient(q)` is `±1`, and some formed
six-neighbor `r` has split HOLD, `Orient(r)` `±1`, and the 3×3 integer
matrix sending the columns of `F(q)` to the columns of `F(r)` is a signed
permutation with determinant `Orient(q)Orient(r)`. If split or Orient
fails at `q`, transport fails, not `UNDEFINED`. Neighbor-read of that
transport HOLDs at `q` if and only if transport HOLDs at `q` and some
formed six-neighbor `r` in `B_3(0)` has transport HOLD. If transport fails
at `q`, neighbor-read fails, not `UNDEFINED`. Q0 = formed-at-τ sites q in
B_3(0) with q_1=0. Q1 = formed-at-τ sites q in B_3(0) with q_1=1. Empty Q0
or Q1 is fail, not UNDEFINED. Reverse HOLDs if and only if Q0 is nonempty
and neighbor-read of transport HOLDs at every `q` in Q0. Face HOLDs if and
only if Q1 is nonempty and neighbor-read of transport HOLDs at every `q`
in Q1. This is not leftover of site-local transport plane-support. That
leftover scores transport HOLD at every formed site on the plane, not
neighbor-read of that transport. On this member the Q0/Q1 neighbor-read
bits coincide with the site-local transport bits; the objects still
differ: neighbor-read inspects a formed six-neighbor's transport HOLD
bit, not the signed-permutation sending. HOLDING existential neighbor-read
of transport on the four z-probes #7511 reverse HOLDs and face HOLDs while
this plane forall fails. Universal 6-NN neighbor-read fail/fail #7556 is a
different leftover: it scores every formed six-neighbor of a probe, not
every formed site on a coordinate plane. Not a 6-NN forall. This is not
leftover of early-tick plane support, which HOLDs on the `t<=1` subset of
Q0 and of Q1 while the full planes fail. This is not leftover of nm2cycfrmz
cyclic-frame transport on four z-probes. This is not leftover of
existential neighbor-read. This is not leftover of universal 6-NN
neighbor-read. This is not leftover of nm2axz axis-cover. This is not
leftover of nm2ax12z 1-in 2-out split. This is not leftover of leftover-of-`M`
alone. This is not leftover of leftover-of-`O` alone. This is not
leftover-empty fail of leftover axis. This is not leftover of nmunopp
union. This is not leftover of nmt2opp `M` frozen at `t`. This is not
leftover of nmot2opp two-tick composition. This is not leftover of nmoutopp
untimed eventual-`O`. This is not leftover of mixed #7188 fail/fail. This
is not leftover of the 1-axis opposite two-site seed. This is not leftover
of the same-lock two-site seed. The second pair is a new seed, not a formed
child. Uniqueness is not required. Mixed remains a set. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_x0_plane_support_neighbor_read_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_x0_plane_support_neighbor_read_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the formed sites with `q_1=0` or `q_1=1`. Incoming lock letters are unit
nearest-neighbor steps. `O` is the outgoing dual of those incoming sets at
the per-site cut `τ=t+1`. Axis is the unsigned lattice direction of a signed
lock. Cover is the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)`
and `Axis(O)`. Split is cover together with `|Axis(M)|=1`. The cyclic
next/prev lex-largest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m` and the
lex-largest signed outgoing letter on the cyclic next and prev axes of
`Axis(M)` under `+e < −e`. When split HOLDs, `F=(m,o_next,o_prev)` is that
LIVE three-axis frame. Transport is existential: some formed six-neighbor
hosts a split-HOLDING frame whose columns are a signed permutation of the
source columns with determinant the product of the two Orient signs.
Neighbor-read HOLDs if and only if transport HOLDs and some formed
six-neighbor in `B_3(0)` has transport HOLD. Reverse and face are scored on
neighbor-read HOLD at every formed-at-τ site of the named plane. Occupancy
of sites is not used. A six-neighbor star is not the letter. O is not M.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of plane support of neighbor-read of cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 on the formed x=0 versus x=1 sites in B_3 of the two-axis opposite seed, Q0/Q1 neighbor-read bits, reverse fail and face fail from those plane foralls; uniqueness of a failing site is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_x0_plane_support_neighbor_read_cyclic_frame_transport_tplus1_reverse_face
target_blocker_text: "display forall neighbor-read of HOLDING cyclic-frame transport on the x=0 versus x=1 formed sites in B_3 at t+1, not leftover of site-local transport plane-support, not leftover of existential neighbor-read #7511, not leftover of universal 6-NN neighbor-read #7556, not leftover of four z-probe transport"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep plane support of neighbor-read of cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 displayed; do not write neighbor-read into Admissibility, do not reduce to site-local transport plane-support, do not reduce to existential neighbor-read, do not reduce to universal 6-NN neighbor-read, do not reduce to nm2cycfrmz sending, do not reduce to equal transport bit including fail, do not reduce to scalar neighbor-read of Orient, do not reduce to unique nonnegative permutation sending, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for plane support of neighbor-read of cyclic-frame transport of (m,o_next,o_prev) of M and O at t+1 on the x=0 versus x=1 formed sites of the two-axis opposite seed and reverse/face from that; displayed, not adopted"
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

No larger host is used. No runner cache is written. The scored sites are
every formed-at-τ site in `B_3(0)` with first coordinate `0` or `1`, not
only the four z-probes

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

Those z-probes remain a leftover contrast: `A` and `C` lie in Q0, `B` and
`D` lie in Q1. These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`,
`C=(0,2,0)`, `D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`,
`B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`. Same process as nm2axz.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. The second pair is a new seed, not a formed
child of the first pair. This seed is not the 1-axis opposite two-site seed
`{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not the perp two-site
seed `+e_1/+e_2`. This seed is not the same-lock two-site seed
`+e_1/+e_1`. This seed is not the z-symmetric three-site seed
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

## Named plane support of neighbor-read of cyclic-frame transport at `τ=t+1`

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

Oriented frame, transport, and neighbor-read at the same cut:

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
and some formed 6-NN r in B_3(0) has transport(r) HOLD.
If transport fails at q, neighbor-read fails, not UNDEFINED.
UNDEFINED if transport is UNDEFINED.
Uniqueness of r is not required.

Q0 = formed-at-τ sites q in B_3(0) with q_1=0.
Q1 = formed-at-τ sites q in B_3(0) with q_1=1.
Empty Q0 or Q1 is fail, not UNDEFINED.
Reverse HOLDs iff Q0 is nonempty and neighbor-read HOLDs at every q in Q0.
Face HOLDs iff Q1 is nonempty and neighbor-read HOLDs at every q in Q1.
```

Site-local transport plane-support HOLDs if and only if the named plane is
nonempty and transport HOLDs at every listed site. That leftover is not
this letter. Existential neighbor-read of HOLDING #7511 HOLDs if some
formed six-neighbor has transport HOLD and is scored on four z-probes.
Universal 6-NN neighbor-read HOLDs if transport HOLDs, `N(q)` is nonempty,
and every `r` in `N(q)` has transport HOLD. Not a 6-NN forall: Q0 is not
the six-neighbors of a probe.

## Theorem 1 — ticks, Q0, Q1, and neighbor-read bit at each listed site

On this process Q0 and Q1 are nonempty. `|Q0|=27`. `|Q1|=25`. Empty Q0 or
Q1 is fail, not UNDEFINED; neither set is empty. The four z-probes form:
`t((0, 0, 1))=0`, `t((1, 1, 1))=1`, `t((0, 0, 2))=1`, `t((1, 0, 1))=1`.
Origin and the second pair are seeds: `t((0, 0, 0))=0`, `t((0, 1, 0))=0`,
`t((0, 0, 1))=0`, `t((0, 1, 1))=0`. The farthest listed fail on Q0 is at
tick 5: `t((0, -3, 0))=5`.

```text
Q0, lex order, t and neighbor-read:
(0, -3, 0) t=5 neighbor-read=fail
(0, -2, -2) t=4 neighbor-read=fail
(0, -2, -1) t=3 neighbor-read=fail
(0, -2, 0) t=4 neighbor-read=fail
(0, -2, 1) t=3 neighbor-read=fail
(0, -2, 2) t=4 neighbor-read=fail
(0, -1, -2) t=3 neighbor-read=fail
(0, -1, -1) t=2 neighbor-read=fail
(0, -1, 0) t=1 neighbor-read=hold
(0, -1, 1) t=2 neighbor-read=fail
(0, -1, 2) t=2 neighbor-read=fail
(0, 0, -3) t=5 neighbor-read=fail
(0, 0, -2) t=4 neighbor-read=fail
(0, 0, -1) t=1 neighbor-read=hold
(0, 0, 0) t=0 neighbor-read=hold
(0, 0, 1) t=0 neighbor-read=hold
(0, 0, 2) t=1 neighbor-read=hold
(0, 1, -2) t=4 neighbor-read=fail
(0, 1, -1) t=1 neighbor-read=hold
(0, 1, 0) t=0 neighbor-read=hold
(0, 1, 1) t=0 neighbor-read=hold
(0, 1, 2) t=1 neighbor-read=hold
(0, 2, -2) t=3 neighbor-read=fail
(0, 2, -1) t=2 neighbor-read=fail
(0, 2, 0) t=1 neighbor-read=hold
(0, 2, 1) t=2 neighbor-read=fail
(0, 2, 2) t=2 neighbor-read=fail

Q1, lex order, t and neighbor-read:
(1, -2, -2) t=5 neighbor-read=fail
(1, -2, -1) t=4 neighbor-read=fail
(1, -2, 0) t=3 neighbor-read=hold
(1, -2, 1) t=4 neighbor-read=fail
(1, -2, 2) t=4 neighbor-read=fail
(1, -1, -2) t=4 neighbor-read=fail
(1, -1, -1) t=3 neighbor-read=fail
(1, -1, 0) t=2 neighbor-read=hold
(1, -1, 1) t=2 neighbor-read=hold
(1, -1, 2) t=3 neighbor-read=fail
(1, 0, -2) t=3 neighbor-read=hold
(1, 0, -1) t=2 neighbor-read=hold
(1, 0, 0) t=2 neighbor-read=fail
(1, 0, 1) t=1 neighbor-read=hold
(1, 0, 2) t=2 neighbor-read=fail
(1, 1, -2) t=3 neighbor-read=hold
(1, 1, -1) t=2 neighbor-read=hold
(1, 1, 0) t=2 neighbor-read=fail
(1, 1, 1) t=1 neighbor-read=hold
(1, 1, 2) t=2 neighbor-read=fail
(1, 2, -2) t=4 neighbor-read=fail
(1, 2, -1) t=3 neighbor-read=fail
(1, 2, 0) t=2 neighbor-read=fail
(1, 2, 1) t=2 neighbor-read=hold
(1, 2, 2) t=3 neighbor-read=fail

neighbor-read((0, -3, 0)) = fail
neighbor-read((0, 0, 0)) = hold
neighbor-read((0, 0, 1)) = hold
neighbor-read((1, -2, -2)) = fail
neighbor-read((1, 0, 1)) = hold
neighbor-read((1, 1, 1)) = hold
hold-count(Q0) = 10
fail-count(Q0) = 17
hold-count(Q1) = 10
fail-count(Q1) = 15
fail-witness(Q0) = (0, -3, 0)
fail-witness(Q1) = (1, -2, -2)
```

On this member the Q0/Q1 neighbor-read bits coincide with the site-local
transport bits. The objects still differ: neighbor-read inspects a formed
six-neighbor's transport HOLD bit, not the signed-permutation sending of
`F(q)` to `F(r)`. At `(0,-1,1)` transport fails, so neighbor-read fails,
not `UNDEFINED`; equal transport bits including fail=fail HOLDs there
because a formed six-neighbor also fails. Existential neighbor-read HOLDs
at each of the four z-probes. Universal 6-NN neighbor-read HOLDs at `A` and
fails at `B`, `C`, and `D`. Cover and split HOLD at each of those four
z-probes and do not score the plane forall.

Early-tick restriction `t<=1` of Q0 is ten sites, all neighbor-read HOLD.
Early-tick restriction of Q1 is `((1, 0, 1), (1, 1, 1))`, both HOLD. That
early-tick plane support HOLDs while the full planes fail. The y=0 formed
plane fails. The x=−1 formed plane fails. The x=3 formed plane is empty
and is fail, not UNDEFINED.

On the 1-axis opposite two-site seed, Q0 and Q1 neighbor-read plane
supports fail. On the same-lock two-site seed they fail. On the LIVE
three-axis seed they fail. Those seeds are leftover.

## Theorem 2 — reverse from plane support of neighbor-read of cyclic-frame transport at `τ`

Reverse HOLDs if and only if Q0 is nonempty and neighbor-read HOLDs at
every `q` in Q0. Q0 is nonempty. Neighbor-read fails at
`fail-witness(Q0) = (0, -3, 0)`. Reverse fails. This is HOLD iff the
x=0 plane forall of neighbor-read HOLDs, not leftover of site-local
transport plane-support, not leftover of nm2cycfrmz cyclic-frame transport
sending on four z-probes whose reverse HOLDs, not leftover of existential
neighbor-read of HOLDING #7511 whose reverse HOLDs, not leftover of
universal 6-NN neighbor-read fail/fail #7556, not leftover of equal
transport bits including fail=fail, not leftover of nm2oricyclz cyclic
Orient equal signs, not leftover of scalar neighbor-read, not leftover of
a unique nonnegative permutation sending, not leftover of nm2axz
axis-cover, not leftover of nm2ax12z 1-in 2-out split, not leftover-empty
fail, not leftover of early-tick plane support, and not exist-opposite.

Reverse x=0 plane support of neighbor-read of cyclic-frame transport at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Existential neighbor-read reverse HOLDs because existential neighbor-read
HOLDs at `A` and at `B`. Transport reverse HOLDs because transport HOLDs
at `A` and at `B`. Site-local transport plane-support reverse fails with
the same first fail-witness; that leftover still scores transport, not
neighbor-read. This reverse fails because a formed site on `q_1=0` has
neighbor-read fail. Early-tick x=0 plane support HOLDs. Universal 6-NN
reverse fails because universal neighbor-read fails at `B`. Those leftovers
are not this display.

Reverse fails.

## Theorem 3 — face from plane support of neighbor-read of cyclic-frame transport at `τ`

Face HOLDs if and only if Q1 is nonempty and neighbor-read HOLDs at every
`q` in Q1. Q1 is nonempty. Neighbor-read fails at
`fail-witness(Q1) = (1, -2, -2)`. Face fails.

Face x=1 plane support of neighbor-read of cyclic-frame transport at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face HOLDs because cover HOLDs at `C` and at `D`. Split face HOLDs
because split HOLDs at `C` and at `D`. Existential neighbor-read face HOLDs
because existential neighbor-read HOLDs at `C` and at `D`. Transport face
HOLDs because transport HOLDs at `C` and at `D`. Site-local transport
plane-support face fails with the same first fail-witness; that leftover
still scores transport, not neighbor-read. This face fails because a formed
site on `q_1=1` has neighbor-read fail. Early-tick x=1 plane support HOLDs.
Universal 6-NN face fails because universal neighbor-read fails at `C` and
at `D`. Those leftovers are not this display.

Face fails.

## What this note does not claim

- It does not replace plane support of neighbor-read by site-local transport plane-support.
- It does not replace plane support of neighbor-read by existential neighbor-read of HOLDING #7511.
- It does not replace plane support of neighbor-read by universal 6-NN neighbor-read fail/fail #7556.
- It does not replace neighbor-read of transport by nm2cycfrmz signed-permutation sending.
- It does not replace neighbor-read by equal transport bits including fail=fail.
- It does not replace neighbor-read of transport by neighbor-read of the scalar Orient sign.
- It does not replace neighbor-read of transport by a unique nonnegative permutation sending.
- It does not require a unique formed six-neighbor witness.
- It does not reprint nm2oricyclz cyclic Orient reverse hold face hold as this plane forall.
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
  plane forall.
- It does not reprint nm2axz axis-cover reverse hold face hold as this
  plane forall.
- It does not reprint nm2ax12z 1-in 2-out split reverse hold face hold as
  this plane forall.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not score only the y-probes or only the x-probes as this letter.
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

This display uses Lattice to name `B_3(0)` and the formed sites with
`q_1=0` or `q_1=1`. It uses Qubit only as the algebra of the local
possibility domain. It uses Record only as a boundary: a present lock is
content. It does not rewrite Admissibility. The two-axis opposite seed
process, neighbor-read of cyclic-frame transport of `(m,o_next,o_prev)` of
`M` and `O` at `t+1`, and the reverse/face bits from that plane forall are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| Q0 formed-at-τ sites with `q_1=0` | Theorem 1; `|Q0|=27` |
| Q1 formed-at-τ sites with `q_1=1` | Theorem 1; `|Q1|=25` |
| ticks at listed sites | Theorem 1; `t((0, 0, 0))=0`, `t((0, 0, 1))=0`, `t((1, 1, 1))=1`, `t((0, -3, 0))=5` |
| neighbor-read of transport at each listed site | Theorem 1; hold-count(Q0)=10, fail-count(Q0)=17, hold-count(Q1)=10, fail-count(Q1)=15 |
| reverse from x=0 plane forall of neighbor-read at `τ` | Theorem 2; `fail` |
| face from x=1 plane forall of neighbor-read at `τ` | Theorem 3; `fail` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| leftover of site-local transport plane-support | not this letter |
| leftover of existential neighbor-read #7511 | not this plane forall |
| leftover of universal 6-NN neighbor-read #7556 | not this plane forall |
| leftover of nm2cycfrmz cyclic-frame transport sending | not this neighbor-read |
| leftover of equal transport bits including fail=fail | not this neighbor-read |
| leftover of scalar neighbor-read of Orient | not this neighbor-read |
| leftover of unique nonnegative permutation sending | not this neighbor-read |
| leftover of nm2oricyclz cyclic Orient equal signs | not this neighbor-read |
| leftover of nm2axz axis-cover HOLD | not this plane forall |
| leftover of nm2ax12z 1-in 2-out split HOLD | not this plane forall |
| leftover of leftover-empty fail of leftover axis | not this display |
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
| leftover of early-tick plane support | not this display |
| split fail scored as `UNDEFINED` | refused; neighbor-read fail |
| empty plane scored as `UNDEFINED` | refused; fail, not UNDEFINED |
| global later T | not used |
| neighbor-read as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: forall formed sites on the x=0 plane, neighbor-read of cyclic-frame transport HOLDs, versus the x=1 plane, and reverse/face from that. |
| V2 | Current main has no landed plane support of neighbor-read of cyclic-frame-transport reverse/face of timed `M` and `O` on the formed x=0 versus x=1 sites of the two-axis opposite seed. |
| V3 | Neighbor-read reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it scores neighbor-read HOLD at every formed-at-τ site of a coordinate plane, reverse fails and face fail while four z-probe existential neighbor-read reverse HOLDs and face HOLDs, universal 6-NN reverse fails from a 6-NN forall not a plane forall, site-local transport plane-support scores a different object, and early-tick plane support HOLDs while the full planes fail. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace neighbor-read by site-local
transport plane-support, does not replace neighbor-read by existential
neighbor-read of four z-probes, does not replace neighbor-read by
universal 6-NN neighbor-read, does not replace neighbor-read by nm2cycfrmz
sending, does not replace neighbor-read by equal transport bits including
fail=fail, does not replace neighbor-read by scalar neighbor-read of
Orient, does not replace neighbor-read by nm2axz axis-cover, does not
replace neighbor-read by nm2ax12z 1-in 2-out split, does not identify this
display with the 1-axis opposite two-site seed, and does not identify it
with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| site-local transport plane-support | reuse transport HOLD at every formed site on x=0 versus x=1 | that leftover scores transport, not neighbor-read of a formed 6-NN's transport HOLD bit; on this member the Q0/Q1 bits coincide, but the objects differ and four z-probe transport reverse HOLDs while this plane forall fails | ATTEMPTED |
| existential neighbor-read #7511 | reuse some formed 6-NN with transport HOLD on four z-probes | existential reverse HOLDs and face HOLDs while this reverse fails and this face fails; Q0 is not a 6-NN star of a probe | ATTEMPTED |
| universal 6-NN neighbor-read #7556 | require every r in N(q) to transport | universal reverse fails and face fails from a 6-NN forall, not a coordinate-plane forall; universal HOLDs at A while this Q0 forall fails | ATTEMPTED |
| nm2cycfrmz cyclic-frame transport sending | reuse signed-permutation sending of F(q) to F(r) | sending inspects P; this neighbor-read reads only the transport HOLD bit at a formed 6-NN. Four z-probe transport reverse HOLDs while this reverse fails | ATTEMPTED |
| equal transport bits including fail=fail | HOLD if some formed 6-NN has the same transport bit | at (0,-1,1) transport fails and a formed 6-NN also fails, so equal-bit HOLDs while neighbor-read fails, not UNDEFINED | ATTEMPTED |
| scalar neighbor-read of Orient | reuse equal Orient sign at some formed 6-NN | scalar HOLDs at A and fails at B,C,D; scalar reverse fails and scalar face fails | ATTEMPTED |
| unique nonnegative permutation sending | require a unique sending with no minus signs | unique nonnegative sending fails at each of A,B,C,D | ATTEMPTED |
| nm2oricyclz cyclic Orient | reuse Orient reverse hold and face hold from equal ±1 signs | Orient reverse HOLDs and face HOLDs without a plane forall of neighbor-read | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse hold and cover face hold on these z-probes | cover HOLDs reverse and face without neighbor-read of transport | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse split reverse hold and split face hold | split HOLDs reverse and face without neighbor-read; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails and leftover face fails from empty leftover, not from a plane forall of neighbor-read | ATTEMPTED |
| leftover of M alone | score {e_1,e_2,e_3} minus Axis(M) | leftover of M reverse fails from nonempty unequal leftover axes | ATTEMPTED |
| leftover of O alone | score {e_1,e_2,e_3} minus Axis(O) | leftover of O reverse fails from nonempty unequal leftover axes | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of M and of O | exist-opposite face of signed O fails while four z-probe neighbor-read face HOLDs; this face fails from a different object | ATTEMPTED |
| early-tick plane support | restrict Q0 and Q1 to t<=1 | early-tick reverse HOLDs and early-tick face HOLDs while the full planes fail | ATTEMPTED |
| y=0 or x=−1 plane | score a different coordinate plane | those planes fail; this letter is q_1=0 versus q_1=1 | ATTEMPTED |
| empty x=3 plane as UNDEFINED | treat an empty formed plane as unformed | empty Q0 or Q1 is fail, not UNDEFINED; x=3 is empty and fail | ATTEMPTED |
| nmunopp untimed union | score reverse/face from M ∪ O | union is signed letters; neighbor-read is a transport HOLD bit at a formed 6-NN | ATTEMPTED |
| unique outgoing letter | replace mixed O by a singleton or UNDEFINED | mixed O remains a set; unique-letter Orient is UNDEFINED while transport can HOLD | ATTEMPTED |
| 2-in 1-out as UNDEFINED | treat \|Axis(M)\|=2 cover as unformed | split fail is transport fail then neighbor-read fail, not UNDEFINED | ATTEMPTED |
| empty O_i as UNDEFINED | treat empty signed outgoing on an axis as unformed | empty O_i is Orient fail, then neighbor-read fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse t(A)=1 and split fail at C | different seed; second pair is a new seed, not a formed child; here t((0, 0, 1))=0 | ATTEMPTED |
| y-probe or x-probe readout | score four y-probes or four x-probes | this letter is the formed x=0 versus x=1 planes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores neighbor-read of cyclic-frame transport at t+1 | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed M reverse-fail face-fail | different process; this member reports plane forall fail/fail on the two-axis opposite seed | ATTEMPTED |
| same-lock two-site seed | reuse +e_1/+e_1 | different seed; this member is two disjoint opposite pairs | ATTEMPTED |
| LIVE three-axis three-site seed | reuse +e_1/+e_2/+e_3 | different seed; LIVE three-axis is the frame, not this plane forall | ATTEMPTED |
| sum of a set | replace neighbor-read by a Z^3 sum | the construction does not sum | ATTEMPTED |
| named-sign lettering | collapse {±e_i} to {+,−} | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until max t before reading | τ(q)=t(q)+1 is per-site; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form sites by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of neighbor-read with
site-local transport plane-support, missing identification of neighbor-read
with existential neighbor-read of four z-probes, missing identification of
neighbor-read with universal 6-NN neighbor-read, missing identification of
neighbor-read with nm2cycfrmz sending, missing identification of
neighbor-read with equal transport bits including fail=fail, missing
identification of neighbor-read with nm2axz axis-cover, missing
identification of neighbor-read with nm2ax12z 1-in 2-out split, missing
identification of this seed with the 1-axis opposite two-site seed, and
missing Record identification of the plane bits are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-site `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
next/prev axes of `Axis(M)`, lex-largest signed outgoing letter under
`+e < −e` (hence `−e` if both signs), integer determinant sign, empty
`O_next` or empty `O_prev` as Orient fail not `UNDEFINED`, split fail as
Orient fail not `UNDEFINED`, Q0 as formed-at-τ sites with `q_1=0`, Q1 as
formed-at-τ sites with `q_1=1`, empty plane as fail not `UNDEFINED`, second
pair as a new seed not a formed child, and mixed remains a set are
declared. No uniqueness of outgoing locks, no six-neighbor lock union as
the scored object, no lock-count clock, no global later T, no formation
attachment from already-recorded six-neighbor locks, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
neighbor-read `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | neighbor-read of the cyclic-frame transport HOLD bit at a formed 6-NN | no continuum alphabet |
| per site | formed sites with q_1=0 and q_1=1 in Euclidean B_3(0) | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | Q0/Q1 neighbor-read reports, reverse/face from those plane foralls | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for plane support of
neighbor-read of cyclic-frame transport reverse/face, a formation-rate
rule, and a physical selector among 1-in 2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Plane forall fail/fail is only leftover of site-local
transport plane-support, or of existential neighbor-read of HOLDING #7511,
or of universal 6-NN neighbor-read fail/fail #7556, or of nm2cycfrmz
cyclic-frame transport sending, or of equal transport bits including
fail=fail, or of nm2oricyclz cyclic Orient equal signs, or of neighbor-read
of the scalar Orient sign, or of cover and split; leftover-axis already
answers reverse HOLD; lex-one already answers face HOLD; mixed #7188
already reported fail/fail; the second pair is only the formed child
`(0,0,1)` of the 1-axis seed; unique outgoing letters should be required;
and the Q0/Q1 neighbor-read bits equal the transport bits so the objects
are the same.

**Answer:** Site-local transport plane-support scores transport HOLD at
every formed site on the plane. This letter scores neighbor-read HOLD at
every formed site on the plane. On this member the Q0/Q1 bits coincide;
the objects still differ because neighbor-read inspects a formed
six-neighbor's transport HOLD bit, not the signed-permutation sending.
Existential neighbor-read reverse HOLDs and face HOLDs on the four z-probes
while this reverse fails and this face fails. Universal 6-NN neighbor-read
is a 6-NN forall, not a coordinate-plane forall; Not a 6-NN forall.
Four z-probe transport reverse HOLDs while this reverse fails. Equal
transport bits including fail=fail HOLDs at `(0,-1,1)` while neighbor-read
fails there, not UNDEFINED. Cover and split HOLD reverse and face on the
four z-probes and do not score the plane forall. Early-tick plane support
HOLDs while the full planes fail. Mixed #7188 is a different z-symmetric
process with mixed `M`. The second pair is a new seed, not a formed child:
`(0,0,1)` is recorded at tick 0 with lock `+e_2`, whereas the 1-axis child
forms at tick 1 with lock `+e_3`. Reverse plane support is HOLD iff every
formed x=0 site has neighbor-read HOLD, not leftover of four-probe
existential neighbor-read and not leftover of site-local transport
plane-support.

### N8 — cross-cycle echo

nm2axz cover on this two-axis seed reported cover HOLD at each of the four
z-probes, reverse hold, and face hold. nm2ax12z 1-in 2-out split on the
same seed reported split HOLD at each of the four z-probes, reverse hold,
and face hold. nm2oricyclz cyclic next/prev lex-largest Orient on the same
seed reported HOLDING cyclic #7451/#7452 with Orient `−1,−1,+1,+1`, reverse
hold, and face hold from equal signs, without a sending matrix. nm2cycfrmz
cyclic-frame transport on the same seed reported transport HOLD at each of
the four z-probes, reverse hold, and face hold. Existential neighbor-read
of that transport #7511 reported neighbor-read HOLD at each of the four
z-probes, reverse hold, and face hold. Universal 6-NN neighbor-read #7556
reported reverse fail and face fail from a 6-NN forall. Site-local
transport plane-support reported reverse fail and face fail from transport
HOLD at every formed x=0 versus x=1 site. This note is not those displays:
it reports plane support of neighbor-read of cyclic-frame transport of
`(m,o_next,o_prev)` of `M` and `O` at `τ=t+1` on the two-axis opposite
seed, with `|Q0|=27`, `|Q1|=25`, hold-count(Q0) = 10, fail-count(Q0) = 17,
hold-count(Q1) = 10, fail-count(Q1) = 15, reverse fail, and face fail.
Cover and split do not score handedness.

**Gate disposition:** PASS for the plane-support of neighbor-read of
cyclic-frame-transport `t+1` reverse/face reports above. FAIL / DO NOT SHIP
for “the predicate equals site-local transport plane-support,” “the
predicate equals existential neighbor-read of HOLDING #7511,” “the
predicate equals universal 6-NN neighbor-read,” “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals nm2oricyclz cyclic Orient
HOLD,” “the predicate equals nm2cycfrmz cyclic-frame transport sending
HOLD,” “the predicate equals equal transport bits including fail=fail
HOLD,” “the predicate equals scalar neighbor-read of Orient HOLD,” “the
predicate equals unique nonnegative permutation sending HOLD,” “the
predicate equals nm2axz axis-cover HOLD,” “the predicate equals nm2ax12z
1-in 2-out split HOLD,” “the predicate equals the 1-axis opposite two-site
seed,” “the predicate equals nmunopp union,” “the predicate equals
early-tick plane support HOLD,” “bits are Admissibility,” “split fail is
UNDEFINED,” or “empty Q0 or Q1 is UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, lists Q0 and Q1, reads each formed site's
own earliest incoming set and own outgoing dual from the record prefix at
that site's `t+1`, reports transport as nm2cycfrmz by a signed-permutation
sending to some formed six-neighbor, reports neighbor-read of that
transport HOLD bit at a formed six-neighbor in `B_3(0)`, and checks
Theorems 1--3. It also checks that empty Q0 or Q1 is fail not `UNDEFINED`,
that reverse fails and face fails from the plane foralls while four z-probe
existential neighbor-read reverse HOLDs and face HOLDs, that universal 6-NN
reverse fails and face fails, that early-tick plane support HOLDs, that
site-local transport plane-support is a different function, that transport
fail is neighbor-read fail not `UNDEFINED`, that equal transport bits
including fail=fail HOLDs at `(0,-1,1)` while neighbor-read fails there,
that the 1-axis opposite two-site seed is a different member, that #7477
same-lock is a different member, that LIVE three-axis is a different
member, that mixed #7188 is a different process, and that no runner cache
is written. It does not attach L1. It does not write into Admissibility.
This is not the two-tick lock-count clock composition.
