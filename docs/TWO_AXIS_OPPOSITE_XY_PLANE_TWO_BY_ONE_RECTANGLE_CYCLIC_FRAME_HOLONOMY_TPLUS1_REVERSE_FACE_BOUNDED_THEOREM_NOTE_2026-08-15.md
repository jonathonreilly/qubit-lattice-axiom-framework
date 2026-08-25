---
claim_id: two_axis_opposite_xy_plane_two_by_one_rectangle_cyclic_frame_holonomy_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic-frame holonomy around the 2-by-1 xy rectangle at t+1 on the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_xy_plane_two_by_one_rectangle_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py
---

# Cyclic-Frame Holonomy Around The 2-By-1 Xy Rectangle At t+1 Reverse And Face

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact six-edge cyclic-frame holonomy of the 2-by-1 xy rectangle at
`z=1` and of the parallel rectangle at `z=0`, at the common cut `τ=t+1` on
the two-axis opposite seed in Euclidean `B_3(0)`. Reverse and face from those
products. Not a unit square. Not a yz 2-by-1 rectangle.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_xy_plane_two_by_one_rectangle_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_xy_plane_two_by_one_rectangle_cyclic_frame_holonomy_tplus1_reverse_face_2026_08_15.py)

## Result up front

Cyclic-frame transport along a named directed edge is the signed-permutation
map of the ordered triple `F=(m,o_next,o_prev)`, with `P` as in the directed
two-step display along `+e_1`. This note displays the *six-edge product*
around the 2-by-1 xy rectangle

```text
(0,0,1) --e1--> (1,0,1) --e1--> (2,0,1) --e2--> (2,1,1)
        --(-e1)--> (1,1,1) --(-e1)--> (0,1,1) --(-e2)--> (0,0,1)
```

versus the parallel rectangle at `z=0`. It is not a unit square and not a
yz 2-by-1.

At the common cut `τ=t+1` of the seeds (`t=0`, so `τ=1`), both rectangles
have vertices in `B_3(0)`, but not every vertex is formed with split HOLD and
a signed-permutation `P` on every edge. Therefore both products fail, and

```text
reverse: fail
face: fail
```

The bits are Displayed, not adopted. Do not write into Admissibility. Do not attach L1. Uniqueness is not required.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact six-edge holonomy products on Euclidean B_3(0) at one declared cut; the bits are displayed and not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_xy_plane_two_by_one_rectangle_cyclic_frame_holonomy_tplus1_reverse_face_bounded_theorem_note_2026-08-15
target_blocker_text: "display six-edge cyclic-frame holonomy of the 2-by-1 xy rectangle at t+1 and the reverse/face pair from those products"
source_of_blocker_text: frontier_question
reachability_to_target: closed_finite_target
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "exact only for the declared two-axis opposite seed, Euclidean B_3(0), and the named 2-by-1 xy rectangles at t+1"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility does not supply the formation site, probability, or rate. The
perp-step incoming-lock process used below is a declared finite host process,
not an axiom edit. Do not write into Admissibility.

## Exact objects

Euclidean B_3(0)={n:n·n<=9} inside `Z^3`. No larger ball is used. Nearest
neighbors are the six axial steps `{±e_1,±e_2,±e_3}` with
`e_1=(1,0,0)`, `e_2=(0,1,0)`, `e_3=(0,0,1)`.

Seed at tick `0`, two disjoint opposite pairs:

```text
(0,0,0) locks +e_1
(0,1,0) locks -e_1
(0,0,1) locks +e_2
(0,1,1) locks -e_2
```

From a recorded site `p` with unique lock `L(p)=±e_i`, a step `s` to
`q=p+s` is allowed iff `s·e_i=0`. If `q` lies in `B_3(0)` and is unformed,
`q` forms at `t(p)+1` and the incoming set `M(q)` is the set of earliest such
steps. If that set is not a singleton, `q` has no unique lock and does not
emit. Seed incoming sets are the assigned locks.

Let `t(q)` be the formation tick. The cut is `τ=t+1`. For the seed process,
`t=0` so `τ=1`. A site is formed at `τ` iff it is recorded with tick `≤ τ`.
Unformed at `τ` is fail, not UNDEFINED. A vertex outside `B_3(0)` is fail, not
UNDEFINED.

`M(q,τ)` is the earliest incoming set of `q` from records with tick `≤ τ`,
defined only if `q` is formed at `τ`.

`O(q,τ)={e in {±e_1,±e_2,±e_3} | q+e formed at τ and e in M(q+e,τ)}`.

`Axis(S)={e_i | some ±e_i in S}`. Cover holds iff `Axis(M)∩Axis(O)` is empty
and `Axis(M)∪Axis(O)={e_1,e_2,e_3}`. Split holds iff cover holds and
`|Axis(M)|=1` with `m` unique in `M`. Two-in one-out is fail. If split fails,
Orient fails, not UNDEFINED.

When split holds, let `i` be the axis index of `m`. Set `e_next=e_{i+1}` with
`3+1→1` and `e_prev=e_{i-1}` with `1-1→3`. Let
`O_next=O∩{±e_next}` and `O_prev=O∩{±e_prev}`. If either is empty, Orient
fails, not UNDEFINED. Order `+e < -e`. Then `o_next` is the lex-largest
vector in `O_next` (hence `-e` if both signs), and `o_prev` likewise.
`F(q)` is the `3×3` integer matrix with columns `(m,o_next,o_prev)`.
`Orient(q)` is the sign of `det F(q)`. Split plus nonempty leftover axes
makes `Orient∈{±1}` and makes `F` a signed permutation matrix.

Directed-edge HOLD from `q` to `q+e` iff `q` and `q+e` lie in `B_3(0)`, both
are formed at `τ`, split holds at both, Orient is `±1` at both, and the unique
`3×3` integer matrix `P` sending columns of `F(q)` to columns of `F(q+e)`
(the unique `P` with `P F(q)=F(q+e)`) is a signed permutation with
`det P=Orient(q)Orient(q+e)`. Else that edge fails, not UNDEFINED.

Holonomy of a rectangle HOLDs iff every vertex of the six-edge cycle is in
`B_3(0)` and formed, split HOLDs at every vertex, Orient is `±1` at every
vertex, every edge has `P`, and the `3×3` product of the six `P` in cycle
order is the identity. Else that rectangle fails, not UNDEFINED.

Reverse rectangle at `z=1`: the six-edge cycle above. Face rectangle at
`z=0`: origin `--e1-->` `(1,0,0)` `--e1-->` `(2,0,0)` `--e2-->` `(2,1,0)`
`--(-e1)-->` `(1,1,0)` `--(-e1)-->` `(0,1,0)` `--(-e2)-->` origin.
Reverse HOLD iff holonomy of the `z=1` rectangle HOLDs. Face HOLD iff
holonomy of the `z=0` rectangle HOLDs.

## Theorem 1

At `τ=1` the four seeds are formed at tick `0`. The tick-1 records in
`B_3(0)` are exactly fourteen sites: the four seeds together with

```text
(0,-1,0)  M={-e_2}
(0,0,-1)  M={-e_3}
(0,2,0)   M={+e_2}
(0,1,-1)  M={-e_3}
(1,0,1)   M={+e_1}
(-1,0,1)  M={-e_1}
(0,0,2)   M={+e_3}
(1,1,1)   M={+e_1}
(-1,1,1)  M={-e_1}
(0,1,2)   M={+e_3}
```

Frames at the four seeds:

```text
F((0,0,0)) columns (+e_1,-e_2,-e_3); Orient((0,0,0))=+1
F((0,1,0)) columns (-e_1,+e_2,-e_3); Orient((0,1,0))=+1
F((0,0,1)) columns (+e_2,+e_3,-e_1); Orient((0,0,1))=-1
F((0,1,1)) columns (-e_2,+e_3,-e_1); Orient((0,1,1))=+1
```

All twelve rectangle vertices lie in `B_3(0)`. Formation ticks on the full
perp-step process, and the twelve directed edges at `τ=1`:

Reverse cycle at `z=1`:

```text
t((0,0,1))=0  formed, split HOLD, Orient=-1
t((1,0,1))=1  formed, split fail (O empty)
t((2,0,1))=4  unformed at τ=1
t((2,1,1))=4  unformed at τ=1
t((1,1,1))=1  formed, split fail (O empty)
t((0,1,1))=0  formed, split HOLD, Orient=+1

(0,0,1)->(1,0,1)  dst split fail; P fail; edge fail
(1,0,1)->(2,0,1)  (2,0,1) unformed at τ=1; P fail; edge fail
(2,0,1)->(2,1,1)  both unformed at τ=1; P fail; edge fail
(2,1,1)->(1,1,1)  src unformed at τ=1; P fail; edge fail
(1,1,1)->(0,1,1)  src split fail; P fail; edge fail
(0,1,1)->(0,0,1)  P=[(1,0,0); (0,-1,0); (0,0,1)]; edge hold
reverse product: fail
```

Face cycle at `z=0`:

```text
t((0,0,0))=0  formed, split HOLD, Orient=+1
t((1,0,0))=2  unformed at τ=1
t((2,0,0))=3  unformed at τ=1
t((2,1,0))=3  unformed at τ=1
t((1,1,0))=2  unformed at τ=1
t((0,1,0))=0  formed, split HOLD, Orient=+1

(0,0,0)->(1,0,0)  (1,0,0) unformed at τ=1; P fail; edge fail
(1,0,0)->(2,0,0)  both unformed at τ=1; P fail; edge fail
(2,0,0)->(2,1,0)  both unformed at τ=1; P fail; edge fail
(2,1,0)->(1,1,0)  both unformed at τ=1; P fail; edge fail
(1,1,0)->(0,1,0)  src unformed at τ=1; P fail; edge fail
(0,1,0)->(0,0,0)  P=[(-1,0,0); (0,-1,0); (0,0,1)]; edge hold
face product: fail
```

This is not leftover of unit-square holonomy at `z=1`, whose four vertices
omit `(2,0,1)` and `(2,1,1)`. This is not leftover of a yz 2-by-1 rectangle,
whose long sides run along `±e_2`.

## Theorem 2

Reverse HOLD iff holonomy of the `z=1` 2-by-1 xy rectangle HOLDs. Five of
the six edges fail, the six-edge product is fail, and the bit is not
UNDEFINED, so reverse: fail.

## Theorem 3

Face HOLD iff holonomy of the `z=0` 2-by-1 xy rectangle HOLDs. Five of the
six edges fail, the six-edge product is fail, and the bit is not UNDEFINED,
so face: fail. Displayed, not adopted. Do not write into Admissibility. Do
not attach L1.

## What this does not show

The packet does not select a physical Record readout, a formation law, or a
unit-square holonomy identity. It does not score a yz 2-by-1 rectangle. It
does not write the displayed bits into Admissibility. It does not attach L1.
It does not enlarge Euclidean `B_3(0)`. It does not claim uniqueness of `F`
among other frame conventions. Face is displayed, not adopted.
